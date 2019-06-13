from rest_framework import viewsets,generics
from Backlog.serializers import BacklogSerializer
from Backlog.models import Backlog
from rest_framework.permissions import AllowAny,IsAuthenticated
from Task.models import Task
from Task.serializers import TaskSerializer
from django.db.models import Q
from rest_framework.decorators import detail_route
from rest_framework.response import Response

class BacklogModelViewSet(viewsets.ModelViewSet):
    
    permission_classes = [AllowAny,]

    serializer_class = BacklogSerializer

    queryset = Backlog.objects.all()

    @detail_route(methods=['get'])
    def Tasks(self, request, pk=None):
        obj = self.get_object()
        ptcps = Task.objects.filter(
            BackLogID=obj.id)
        serializer_context = {"request": request,}
        serializer = TaskSerializer(ptcps, many=True,context=serializer_context)
        return Response(serializer.data)



