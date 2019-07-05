from rest_framework import viewsets, generics
from .models import Scrum, ProjectUserInvitationModel
from .serializers import ScrumSerializer, UserProjectInvitationSerializer
from rest_framework.permissions import AllowAny,IsAuthenticated



class ScrumModelViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny,]
    serializer_class = ScrumSerializer
    queryset = Scrum.objects.all()

class CreateInvitationView(generics.CreateAPIView):
    permission_classes = [AllowAny,]
    serializer_class = UserProjectInvitationSerializer
    queryset = ProjectUserInvitationModel.objects.all()

# class accept_invitation()