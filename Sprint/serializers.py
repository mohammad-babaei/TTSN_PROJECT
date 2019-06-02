from rest_framework import serializers
from .models import sprint

class SprintSerializer(serializers.ModelSerializer):
    class Meta:
        model = sprint
        fields = '__all__'