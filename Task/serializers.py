from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField,HyperlinkedRelatedField
from rest_framework import serializers
# from accounts.serializers import UsersViewSerializer
from .models import Task




class TaskPickerRelatedField(serializers.RelatedField):

    def to_representation(self,value):
        data = (value.username,value.email,value.profile_picture.url)
        # data = {
        #     "username":value.username,
        #     "email":value.email,
        #     "username":value.profile_picture,
        #     }
        return data




class TaskSerializer(serializers.ModelSerializer):

    # picker = HyperlinkedRelatedField(
    #     read_only=True,
    #     view_name='users-detail'
    # )
    picker = TaskPickerRelatedField(read_only = True)
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
