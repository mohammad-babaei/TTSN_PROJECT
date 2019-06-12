from rest_framework import serializers
from .models import Backlog
class BacklogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Backlog
        # fields = ('name','priority','defenition_done','description')
        fields = '__all__'
        read_only_fields = ('priority',)
        # exclude = ('priority',)
    def create(self,validated_data):
        Backlog_list = Backlog.objects.all().order_by("-id")
        if(Backlog_list):
            max_id = Backlog_list[0].id
            print(max_id)
            backlog = Backlog(name = validated_data["name"],definition_done = validated_data["definition_done"],description = validated_data["description"],priority = max_id+1)
            backlog.save()
        else:
            backlog = Backlog(name = validated_data["name"],definition_done = validated_data["definition_done"],description = validated_data["description"],priority = 0)
            backlog.save()
        return validated_data
# class BacklogTaskSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Backlog
#         # fields = ('name','priority','defenition_done','description')
#         fields = ('id')


            
    # def create(self,validated_data):
    #     # idd = validated_data['id']
    #     name = validated_data['name']
    #     priority = validated_data['priority']
    #     defenition_done = validated_data['defenition_done']
    #     description = validated_data['description']
    #     backlog_obj = Backlog(name,property,defenition_done,description)
    #     backlog_obj.save()
    #     return validated_data