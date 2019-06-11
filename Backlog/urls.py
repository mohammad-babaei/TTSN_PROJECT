from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import BacklogModelViewSet,BacklogTaskList
from django.conf.urls import url
Router = DefaultRouter()

Router.register("",BacklogModelViewSet)
# Router.register("Task",BacklogTaskList)

# Router.register("Task",BacklogTaskList,base_name="Task")

urlpatterns = [

    path('', include(Router.urls)),
    # path('Task/',include(Router))


]
