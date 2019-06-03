from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import BacklogModelViewSet

Router = DefaultRouter()

Router.register("",BacklogModelViewSet)

urlpatterns = [

    path('', include(Router.urls)),


]
