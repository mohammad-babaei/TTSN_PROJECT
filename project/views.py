from rest_framework import viewsets, generics
from .models import ProjectUserInvitationModel,Project
from accounts.models import users
from accounts.serializers import UsersViewSerializer
from .serializers import GeneralProjectSerializer, UserProjectInvitationSerializer
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from django.db.models import Q
from Backlog.models import Backlog
from Backlog.serializers import BacklogSerializer
from rest_framework.decorators import detail_route,list_route,action
from Task.models import Task
from Task.serializers import TaskSerializer
 

class ProjectModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated,]
    serializer_class = GeneralProjectSerializer
    queryset = Project.objects.all()
    def perform_create(self, serializer):
        print(self.request.user)
        serializer.save(Creator=self.request.user)
    
    @detail_route(methods=['get'])
    def Backlogs(self, request, pk=None):
        obj = self.get_object()
        ptcps = Backlog.objects.filter(
            ProjectID=obj.id).order_by('priority')
        serializer_context = {"request": request,}
        serializer = BacklogSerializer(ptcps, many=True,context=serializer_context)
        return Response(serializer.data)

    @detail_route(methods=['get'],url_name='Tasks', url_path='get_Tasks')
    def Tasks(self, request, pk=None):
        obj = self.get_object()
        ptcps = Backlog.objects.filter(
            ProjectID=obj.id).values('id')
        btcps = Task.objects.filter(BackLogID__in=ptcps)
        serializer_context = {"request": request,}
        serializer = TaskSerializer(btcps, many=True,context=serializer_context)
        return Response(serializer.data)

class CreateInvitationView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated,]
    serializer_class = UserProjectInvitationSerializer
    queryset = ProjectUserInvitationModel.objects.all()

class ViewCollaborators(generics.ListAPIView):
    permission_classes = [IsAuthenticated,]
    serializer_class = UsersViewSerializer
    def get_queryset(self):
        
        project_id = self.kwargs['project_id']
        queryset = ProjectUserInvitationModel.objects.filter((Q(Project=project_id)&Q(accepted=True))).values('email')
        user_queryset = users.objects.filter(email__in=queryset)
        return user_queryset
                

class UpdateInvitationView(generics.ListAPIView):
    permission_classes = [IsAuthenticated,]
    serializer_class = UserProjectInvitationSerializer
    lookup_field = 'key'

    def get_queryset(self):
        queryset = ProjectUserInvitationModel.objects.all()
        key = self.kwargs['key'].lower()
        if key is not None:
            queryset = queryset.filter(key=key)
            if queryset.exists():
                invitation = queryset.first()
                if invitation.accepted != True:
                    invitation.accepted = True
                    invitation.save()               
            else:
                raise ValidationError({"error": ["Not Valid Link."]})
        return queryset
