from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField,HyperlinkedRelatedField
from rest_framework import serializers
# from accounts.serializers import UsersViewSerializer
from .models import Task


class TaskSerializer(serializers.ModelSerializer):

    picker = HyperlinkedRelatedField(
        read_only=True,
        view_name='users-detail'
    )
    class Meta:
        model = Task
        fields = (
        # 'picker2',
        'id',
        'title',
        'description',
        'TaskState',
        'picker',
        'BackLogID',
        # 'SprintID'
        )
