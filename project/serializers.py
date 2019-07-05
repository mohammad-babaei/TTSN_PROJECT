from rest_framework import serializers
from .models import Scrum, ProjectUserInvitationModel
from django.utils.crypto import get_random_string
from django.core.mail import send_mail

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

        inviter = self.context['request'].user

        invitation_object = ProjectUserInvitationModel (
        email = email,
        Project = Project,
        # created = created,
        inviter = inviter,
        key = key,
        )
        invitation_object.save()

        send_mail(
            'invitation by ',#+inviter.username,
            'you are invited to a project by ',#+inviter.username,
            'ttsnproject@gmail.com',
            ['mamaly1155@gmail.com'],
            fail_silently=False,
        )

        return invitation_object