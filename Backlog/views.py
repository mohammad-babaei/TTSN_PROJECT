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
        serializer = TaskSerializer(ptcps, many=True)
        return Response(serializer.data)

# class BacklogTaskList(generics.ListAPIView):
    
#     permission_classes = [AllowAny,]
#     queryset = Backlog.objects.all()

#     serializer_class = BacklogSerializer
    # def get_queryset(self, *args,**kwargs):
    #     queryset_list = Task.objects.all()
    #     query = self.request.GET.get("q")
    #     if query:
    #         queryset_list = queryset_list.filter(
    #                     Q(title = query)
    #         ).distinct()
    #     return queryset_list

 