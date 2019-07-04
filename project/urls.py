from rest_framework.routers import DefaultRouter
from .views import ScrumModelViewSet
from django.urls import include, path

Router = DefaultRouter()


Router.register("",ScrumModelViewSet)

urlpatterns = [

    path('Scrum/', include(Router.urls)),


]