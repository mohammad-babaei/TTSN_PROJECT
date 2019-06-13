from .serializers import TaskSerializer
from rest_framework.permissions import AllowAny,IsAuthenticated
from .models import Task
from rest_framework import viewsets,generics


class TaskModelViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny,]
    serializer_class = TaskSerializer
    queryset  = Task.objects.all()

class TaskListByState(generics.ListAPIView):
    """
    get task list by their state
    """
    permission_classes = [AllowAny,]
    serializer_class = TaskSerializer
    def get_queryset(self):
        queryset = Task.objects.all()
        TaskState = self.kwargs['taskstate']
        if TaskState is not None:
            queryset = queryset.filter(TaskState=TaskState)
        return queryset
