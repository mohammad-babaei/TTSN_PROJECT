from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = (
        'id',
        'description',
        'TaskState',
        'UserID',
        # 'BackLogID',
        # 'SprintID'
        )
    def create(self,validated_data):

        description = validated_data['description']
        TaskState = validated_data['TaskState']
        UserID = validated_data['UserID']

        Task_object = Task (
            description = description,
            TaskState = TaskState,
            UserID = UserID
        )

        Task_object.save()
        return validated_data