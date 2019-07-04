from rest_framework import viewsets
from .models import Scrum
from .serializers import ScrumSerializer
from rest_framework.permissions import AllowAny,IsAuthenticated



class ScrumModelViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny,]
    serializer_class = ScrumSerializer
    queryset = Scrum.objects.all()