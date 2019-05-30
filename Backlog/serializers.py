from rest_framework import serializers
from .models import Backlog
class BacklogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Backlog
        # fields = ('name','priority','defenition_done','description')
        fields = '__all__'
    def create(self,validated_data):
        id = validated_data['id']
        name = validated_data['name']
        priority = validated_data['priority']
        defenition_done = validated_data['defenition_done']
        description = validated_data['description']
        backlog_obj = Backlog(id,name,property,defenition_done,description)
        backlog_obj.save()
        return validated_data