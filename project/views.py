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

class ProjectModelViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny,]
    serializer_class = GeneralProjectSerializer
    queryset = Project.objects.all()
    def perform_create(self, serializer):
        print(self.request.user)
        serializer.save(Creator=self.request.user)

class CreateInvitationView(generics.CreateAPIView):
    permission_classes = [AllowAny,]
    serializer_class = UserProjectInvitationSerializer
    queryset = ProjectUserInvitationModel.objects.all()

class ViewCollaborators(generics.ListAPIView):
    permission_classes = [AllowAny,]
    serializer_class = UsersViewSerializer
    def get_queryset(self):
        
        project_id = self.kwargs['project_id']
        queryset = ProjectUserInvitationModel.objects.filter((Q(Project=project_id)&Q(accepted=True))).values('email')
        user_queryset = users.objects.filter(email__in=queryset)
        return user_queryset
                

class UpdateInvitationView(generics.ListAPIView):
    permission_classes = [AllowAny,]
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