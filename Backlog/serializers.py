from rest_framework import serializers
from .models import Backlog
# class BacklogListSerializer(serializers.ListSerializer):
#     pass

class BacklogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Backlog
        # fields = ('name','priority','defenition_done','description')
        fields = '__all__'
        # read_only_fields = ('priority',)
        # exclude = ('priority',)
        # list_serializer_class = CustomListSerializer
    def create(self,validated_data):
        Backlog_list = Backlog.objects.all()
        # if(not Backlog_list):
        #     validated_data["priority"] = 1
        # else:
        max_id = len(Backlog_list)
        if(validated_data["priority"]==None):
            validated_data["priority"]=max_id+1
        elif (validated_data["priority"]>max_id):
            validated_data["priority"]=max_id+1 
        elif (validated_data["priority"]<max_id):
            # Backlog_list = Backlog.objects.all().order_by("priority")
            for i in range(max_id,validated_data["priority"]-1,-1):
                Backlog.objects.filter(priority=i).update(priority=i+1)

        backlog = Backlog(name = validated_data["name"],definition_done = validated_data["definition_done"],description = validated_data["description"],priority = validated_data["priority"])
        backlog.save()
        return validated_data



            