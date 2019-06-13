from rest_framework import serializers

from django.db.models import Q

from .models import users






class UsersViewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = users
        fields=(
            'username',
            'email',
            'url'
        )





class UserSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(max_length = 100)

    class Meta:
        model = users
        fields = ('id',
        'username',
        'email',
        'password',
        'password2'
        )

        extra_kwargs = {
            'password': {'write_only': True},
            'password2': {'write_only': True},
        }

    def validate_password2(self,value):
        data = self.get_initial()
        password1 = data.get("password")
        password2 = value
        if password1 != password2:
            raise serializers.ValidationError("passwords do not match")
        return data


    def validate_email(self,value):
        user_query_set = users.objects.filter(email = value)

        if user_query_set.first():
            raise serializers.ValidationError("entered email address is taken")
        return value
    
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



class UserLoginSerializer(serializers.ModelSerializer):

    username = serializers.CharField(max_length = 20,required = False,allow_blank = True)
    email = serializers.EmailField(max_length = 50,required = False,allow_blank = True)
    token = serializers.CharField(allow_blank = True,read_only = True)

    class Meta:
        model = users
        fields=(
            'username',
            'password',
            'email',
            'token'
        )

    def validate(self,data):
        found_user = None
        username = data.get("username",None)
        email = data.get("email",None)
        password = data.get("password")

        if not email and not username:
            raise serializers.ValidationError("A username/password is required.")
        
        user = users.objects.filter(Q(email = email) | Q(username = username)).distinct()
        
        if user.exists() and user.count() ==1:
            found_user = user.first()
        else:
            raise serializers.ValidationError("not registered")
        
        if found_user:
            if not found_user.check_password(password):
                raise serializers.ValidationError("wrong password")
        token = "bullshit token"

        return data