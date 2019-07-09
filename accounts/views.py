from .serializers import UserSerializer,UserLoginSerializer,UsersViewSerializer,ProjectListSerializer
from .models import users
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework import viewsets,generics
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK ,HTTP_400_BAD_REQUEST
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.decorators import api_view
from project.models import ProjectUserInvitationModel,Project
from rest_framework.decorators import detail_route,list_route,action
from project.serializers import GeneralProjectSerializer

class UserView(viewsets.ReadOnlyModelViewSet):
    permission_classes=[AllowAny,]
    serializer_class = UsersViewSerializer
    queryset = users.objects.all()
    # @detail_route(methods=['get'],url_path = "Projects")
    # def Projects(self, request, pk=None):
    #     obj = self.get_object()
    #     url = request.build_absolute_uri('?')
    #     url = url.split('/')
    #     url.pop(len(url)-2)
    #     url = '/'.join(url)
    #     utcps = users.objects.filter(url=url).values('email')
    #     ptcps = ProjectUserInvitationModel.objects.filter(
    #         email__in=utcps).values('Project')
    #     serializer_context = {"request": request,}
    #     serializer = GeneralProjectSerializer(ptcps, many=True,context=serializer_context)
    #     return Response(serializer.data)



class ViewCurrentUserInfo(generics.ListAPIView):
    permission_classes = [IsAuthenticated,]
    serializer_class = UsersViewSerializer
    def get_queryset(self):
        current_user = self.request.user
        return [current_user,]

class ViewCurrentUserProjects(generics.ListAPIView):
    permission_classes = [IsAuthenticated,]
    serializer_class = GeneralProjectSerializer
    def get_queryset(self):
        current_user = self.request.user
        ptcps = ProjectUserInvitationModel.objects.filter(
        email=current_user.email).values('Project')
        prbps = Project.objects.filter(id__in = ptcps)
        serializer = GeneralProjectSerializer(prbps, many=True)
        return prbps



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