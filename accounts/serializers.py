from rest_framework import serializers

from .models import users

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = users
        fields = ('id','username','email','password')
        extra_kwargs = {
            'password': {'write_only': True},
        }
    
    def create(self,validated_data):

        username = validated_data['username']
        password = validated_data['password']
        email = validated_data['email']

        user_object = users (
            username = username,
            email = email
        )
        user_object.set_password(password)

        user_object.save()
        return validated_data
