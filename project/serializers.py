from rest_framework import serializers
from .models import Scrum
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