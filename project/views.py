from rest_framework import viewsets, generics
from .models import Scrum, ProjectUserInvitationModel
from .serializers import ScrumSerializer, UserProjectInvitationSerializer,UpdateInvitationSerializer
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError

class ScrumModelViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny,]
    serializer_class = ScrumSerializer
    queryset = Scrum.objects.all()

class CreateInvitationView(generics.CreateAPIView):
    permission_classes = [AllowAny,]
    serializer_class = UserProjectInvitationSerializer
    queryset = ProjectUserInvitationModel.objects.all()


class UpdateInvitationView(generics.ListAPIView):
    permission_classes = [AllowAny,]
    serializer_class = UpdateInvitationSerializer
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