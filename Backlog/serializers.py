from rest_framework import serializers
from .models import Backlog
class BacklogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Backlog
        fields = ('name','priority','defenition_done','description','date')