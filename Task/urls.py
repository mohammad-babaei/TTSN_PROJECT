from django.urls import include, path
from django.conf.urls import url
from rest_framework import routers
from .views import TaskViewSet,TaskCreateAPIView


router = routers.DefaultRouter()


router.register(r'viewtasks', TaskViewSet)
# router.register(r'createtask', TaskCreateAPIView.as_view(), basename='CreateTask')


urlpatterns = [
    path('', include(router.urls)),
    url(r'^createtask/$',TaskCreateAPIView.as_view(),name = 'CreateTask'),

]
