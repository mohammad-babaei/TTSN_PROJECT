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

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        pr = instance.priority
        Backlog_list = Backlog.objects.all()
        max_id = len(Backlog_list)
        for i in range(pr+1,max_id+1):
            Backlog.objects.filter(priority=i).update(priority=i-1)
        self.perform_destroy(instance)        
        return Response(status=status.HTTP_204_NO_CONTENT) 

    @detail_route(methods=['get'])
    def Tasks(self, request, pk=None):
        obj = self.get_object()
        ptcps = Task.objects.filter(
            BackLogID=obj.id)
        serializer_context = {"request": request,}
        serializer = TaskSerializer(ptcps, many=True,context=serializer_context)
        return Response(serializer.data)
    @detail_route(url_path='(?P<slug>[\w-]+)/(?P<what>[\w-]+)')
    def get_by_name(self, request, pk=None,slug=None, what=None):
        print(slug, what)


