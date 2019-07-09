from .serializers import UserSerializer,UserLoginSerializer,UsersViewSerializer,UpdateProfileSerilaizer
from .models import users
from rest_framework.generics import CreateAPIView,RetrieveUpdateAPIView
from rest_framework.views import APIView
from rest_framework import viewsets,generics
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK ,HTTP_400_BAD_REQUEST
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.decorators import api_view





class UserView(viewsets.ReadOnlyModelViewSet):
    permission_classes=[AllowAny,]
    serializer_class = UsersViewSerializer
    queryset = users.objects.all()



class ViewCurrentUserInfo(generics.ListAPIView):
    permission_classes = [IsAuthenticated,]
    serializer_class = UsersViewSerializer
    def get_queryset(self):
        current_user = self.request.user
        return [current_user,]


class UpdateProfileView(RetrieveUpdateAPIView):
    permission_classes = [AllowAny,]
    serializer_class = UpdateProfileSerilaizer
    queryset = users.objects.all()
    # def get_queryset(self):
    #     current_user = self.request.user
    #     queryset = users.objects.filter(id = current_user.id)
    #     if queryset.exists():
    #         user = queryset.first()
    #         user.

class UserCreateAPIView(CreateAPIView):

    permission_classes=[AllowAny,]
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



@api_view()
def null_view(request):
    return Response(status=HTTP_400_BAD_REQUEST)

@api_view()
def complete_view(request):
    return Response("Email account is activated")