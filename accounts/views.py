from .serializers import UserSerializer
from .models import users
from rest_framework.generics import CreateAPIView



class UserCreateAPIView(CreateAPIView):
    serializer_class = UserSerializer
    queryset  = users.objects.all() 