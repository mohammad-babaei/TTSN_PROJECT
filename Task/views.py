from .serializers import TaskSerializer
from rest_framework.permissions import AllowAny,IsAuthenticated
from .models import Task
from rest_framework import viewsets


class TaskModelViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny,]
    serializer_class = TaskSerializer
    queryset  = Task.objects.all()