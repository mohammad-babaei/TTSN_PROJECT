#from django.conf.urls import url,include
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import SprintModelViewSet

Router = DefaultRouter()

Router.register("Sprint",SprintModelViewSet)

urlpatterns = [

    path('', include(Router.urls)),


]
