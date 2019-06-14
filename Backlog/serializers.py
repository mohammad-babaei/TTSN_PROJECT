from rest_framework import serializers
from .models import Backlog

class BacklogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Backlog
        fields = '__all__'


    def create(self,validated_data):
        Backlog_list = Backlog.objects.all()
        max_id = len(Backlog_list)
        if(validated_data["priority"]==None or validated_data["priority"]<=0):
            validated_data["priority"]=max_id+1
        elif (validated_data["priority"]>max_id):
            validated_data["priority"]=max_id+1 
        elif (validated_data["priority"]<max_id):
            for i in range(max_id,validated_data["priority"]-1,-1):
                Backlog.objects.filter(priority=i).update(priority=i+1)
        backlog = Backlog(name = validated_data["name"],definition_done = validated_data["definition_done"],description = validated_data["description"],priority = validated_data["priority"])
        backlog.save()
        validated_data['id'] = backlog.id
        validated_data['create_date'] = backlog.create_date
        return validated_data
            