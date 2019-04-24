from .serializers import UserSerializer,UserLoginSerializer
from .models import users
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK ,HTTP_400_BAD_REQUEST
from rest_framework.permissions import AllowAny



class UserCreateAPIView(CreateAPIView):
    serializer_class = UserSerializer
    queryset  = users.objects.all()

class UserLoginAPIView(APIView):
    permission_classes = [AllowAny,]
    serializer_class = UserLoginSerializer

    def post(self,request,*args, **kwargs):
        data = request.data
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            data_2 = serializer.data
            return Response(data_2,HTTP_200_OK)
        return Response(serializer.errors,HTTP_400_BAD_REQUEST)