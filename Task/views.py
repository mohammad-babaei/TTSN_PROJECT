from rest_framework.generics import CreateAPIView
from .serializers import TaskSerializer
from rest_framework.permissions import AllowAny,IsAuthenticated
from .models import Task
from rest_framework import viewsets


class TaskViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [AllowAny,]
    serializer_class = TaskSerializer
    queryset  = Task.objects.all()


class TaskCreateAPIView(CreateAPIView):
    permission_classes = [AllowAny,]
    serializer_class = TaskSerializer
    queryset  = Task.objects.all()
