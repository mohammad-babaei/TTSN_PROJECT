from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import TaskModelViewSet,TaskListByState
from django.conf.urls import url

Router = DefaultRouter()

Router.register("",TaskModelViewSet)

urlpatterns = [

    path('', include(Router.urls)),
    url(r'^TaskByState/(?P<taskstate>.+)/(?P<ProjectID>[0-9]+)/$',TaskListByState.as_view(),name='tasks by state'),


]
