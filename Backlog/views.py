from rest_framework import viewsets,generics,status
from Backlog.serializers import BacklogSerializer,PrioritylistSerializer
from Backlog.models import Backlog
from rest_framework.permissions import AllowAny,IsAuthenticated
from Task.models import Task
from Task.serializers import TaskSerializer
from django.db.models import Q,Sum,Count
from rest_framework.decorators import detail_route,list_route,action
from rest_framework.response import Response
def plus(temp):
    return temp+1

class BacklogModelViewSet(viewsets.ModelViewSet):
    
    permission_classes = [AllowAny,]

    serializer_class = BacklogSerializer

    queryset = Backlog.objects.all()
    # def get_serializer_class(self):
    #     if self.request.method == 'POST':
    #         return PrioritylistSerializer 

    #     return self.serializer_class

    def list(self, request):
        queryset = Backlog.objects.all().order_by('priority')
        serializer = BacklogSerializer(queryset, many=True)
        return Response(serializer.data)

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
    # @detail_route(methods=['get'],url_path='set_priority/(?P<priority>[0-9]+)')
    # def set_priority(self, request, pk=None priority=None):
    #     print("fuck Backlog man: ",pk,"fuck priority man: ",priority)
    #     return Response("fuck") 
    @detail_route(url_name='priority', url_path='set_priority/(?P<priority>[0-9]+)')
    def set_priority(self, request, pk=None, priority=None):
        # print("fuck Backlog man: ",pk,"fuck priority man: ",priority)
        Backlog_list = list(Backlog.objects.order_by('priority'))
        # for i in range(len(Backlog_list)):
        #     print(Backlog_list[i].id)
        instance = Backlog.objects.filter(id = pk)[0]
        former_priority = instance.priority
        a = Backlog_list.pop(former_priority-1)
        Backlog_list.insert(int(priority)-1,instance)
        # former_priority = instance.priority
        max_id = len(Backlog_list)
        for i in range(max_id):
            idd = Backlog_list[i].id
            Backlog.objects.filter(id=idd).update(priority=i+1)
        # Backlog.objects.filter(priority=).update(priority=priority)
        return Response(status=status.HTTP_200_OK)
    @action(methods=['post'],detail=False,serializer_class=PrioritylistSerializer)
    def set_list_priority(self,request):
        req_data = request.data["priorities"]
        new_priorities=list(map(plus,req_data))
        id_newpriority = []
        for i in range(len(new_priorities)):
            instances= Backlog.objects.filter(priority=i+1)
            if(instances):
                idd = instances[0].id
                id_newpriority.append((idd,new_priorities[i]))
        print(id_newpriority)
        for id_prio in id_newpriority:
            Backlog.objects.filter(id=id_prio[0]).update(priority=id_prio[1])
        return Response("HTTP_200_OK" ,status=status.HTTP_200_OK)

