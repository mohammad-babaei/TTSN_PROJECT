from rest_framework import serializers
from .models import Scrum, ProjectUserInvitationModel
from django.utils.crypto import get_random_string
from django.core.mail import send_mail
from django.db.models import Q

class ScrumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scrum
        fields = (
            'id',
            'Name',
            'StartDate',
            'EndTime',
            'Creator',
            'TeamMembers',
            'ScrumMaster',
            'ProjectManager'

        )

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
        # created = validated_data['created']
        # inviter = validated_data['inviter']
        key = get_random_string(64).lower()

        request = self.context['request']


        inviter = request.user
        inviter_username = inviter.username

        absolute_uri = request.build_absolute_uri()

        invitation_link = absolute_uri+'accept-invite/'+key+'/'

        invitation_object = ProjectUserInvitationModel (
        email = email,
        Project = Project,
        # created = created,
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


class UpdateInvitationSerializer(serializers.ModelSerializer):

    class Meta:

        model = ProjectUserInvitationModel
        fields = (
            'key',
            'accepted',
        )
        lookup_field = 'key'
    def validate(self,data):
        found_invitation = None
        key = data.get('key')
        if not key:
            raise serializers.ValidationError("A key is required.")
        invitation = ProjectUserInvitationModel.objects.filter(Q(key = key))
        if invitation.exists():
            found_invitation = invitation.first()
            found_invitation.accepted = True
            found_invitation.save()
        else:
            raise serializers.ValidationError('not valid link')
        return data