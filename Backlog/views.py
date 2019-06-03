from rest_framework import viewsets
from Backlog.serializers import BacklogSerializer
from Backlog.models import Backlog
from rest_framework.permissions import AllowAny,IsAuthenticated

class BacklogModelViewSet(viewsets.ModelViewSet):
    
    permission_classes = [AllowAny,]

    serializer_class = BacklogSerializer

    queryset = Backlog.objects.all()

