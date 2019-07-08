from rest_framework import serializers
from .models import ProjectUserInvitationModel,Project
from django.utils.crypto import get_random_string
from django.core.mail import send_mail
from django.db.models import Q

class GeneralProjectSerializer(serializers.ModelSerializer):
    # Creator = serializers.StringRelatedField(default=serializers.CurrentUserDefault(), read_only=True)  
    class Meta:
        model = Project 
        fields = '__all__'

class ProjectParticipantsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'


class CollaboratorSerializer(serializers.ModelSerializer):
    class Meta:
        pass

class UserProjectInvitationSerializer(serializers.ModelSerializer):

    class Meta:
        model= ProjectUserInvitationModel
        fields = (
            'email',
            'accepted',
            'created',
            'Project',
            'key',
            'sent',
            'inviter',
        )
        read_only_fields = ('key','sent','inviter','accepted','created',)

    def create(self,validated_data):
        email = validated_data['email']
        Project = validated_data['Project']
        key = get_random_string(64).lower()

        request = self.context['request']


        inviter = request.user
        inviter_username = inviter.username

        absolute_uri = request.build_absolute_uri()

        invitation_link = absolute_uri+'accept-invite/'+key+'/'

        invitation_object = ProjectUserInvitationModel (
        email = email,
        Project = Project,
        inviter = inviter,
        key = key,
        )

        invitation_object.save()

        send_mail(
            'invitation by '+inviter_username,
            'you are invited to a project by '+inviter_username+"\n wanna join? click the link "+invitation_link,
            'ttsnproject@gmail.com',
            [email.email,],
            fail_silently=False,
        )

        return invitation_object