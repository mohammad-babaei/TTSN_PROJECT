from .serializers import SprintSerializer
# from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework import viewsets
from .models import sprint

class SprintModelViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny,]
    serializer_class = SprintSerializer
    queryset = sprint.objects.all()