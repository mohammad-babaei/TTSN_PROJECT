from rest_framework import serializers
from .models import ProjectUserInvitationModel,Project
from django.utils.crypto import get_random_string
from django.core.mail import send_mail
from django.db.models import Q
from accounts.models import users
from rest_framework import exceptions

# class ProjectCollaboratorRelatedField(serializers.RelatedField):
#     def to_representation(self,value):
#         data = (value.id,value.username,value.email,value.profile_picture)




# class ProjectCollaboratorRelatedField(serializers.RelatedField):
#     def to_representation(self,value):
#         data = (value.id,value.username,value.email,value.profile_picture)



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
    email = serializers.EmailField(write_only=True)
    class Meta:
        model= ProjectUserInvitationModel
        fields = (
            'UserID',
            'accepted',
            'created',
            'Project',
            'key',
            'sent',
            'inviter',
            'email'
        )
        read_only_fields = ('key','sent','inviter','accepted','created','UserID',)

    def create(self,validated_data):
        email = validated_data['email']
        Uid = users.objects.filter(email=email)
        if (Uid):
            Uid = Uid[0]
        else:
            raise exceptions.NotFound
        Project = validated_data['Project']
        key = get_random_string(64).lower()

        request = self.context['request']


        inviter = request.user
        inviter_username = inviter.username

        absolute_uri = request.build_absolute_uri()

        invitation_link = absolute_uri+'accept-front/'+key+'/'

        invitation_object = ProjectUserInvitationModel (
        UserID = Uid,
        Project = Project,
        inviter = inviter,
        key = key,
        )

        invitation_object.save()

        send_mail(
            'invitation by '+inviter_username,
            'you are invited to a project by '+inviter_username+"\n wanna join? click the link "+invitation_link,
            'ttsnproject@gmail.com',
            [Uid.email,],
            fail_silently=False,
        )

        return invitation_object
