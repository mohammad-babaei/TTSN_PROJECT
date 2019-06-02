from django.conf.urls import url,include
from rest_framework.routers import SimpleRouter
from .views import SprintModelViewSet

Router = SimpleRouter()

Router.register("Sprint",SprintModelViewSet)

urlpatterns = SimpleRouter.urls
