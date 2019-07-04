from rest_framework.routers import DefaultRouter
from .views import ScrumModelViewSet
from django.urls import include, path
from django.conf.urls import url

Router = DefaultRouter()


Router.register("",ScrumModelViewSet)

urlpatterns = [

    path('Scrum/', include(Router.urls)),
    # url(r'^invitations/accept-invite/(?P<key>\w+)/?$', TaskListByState2.as_view(), name='accept-invite'),
    url(r'^', include('rest_invitations.urls')),


]