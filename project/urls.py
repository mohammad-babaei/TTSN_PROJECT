from rest_framework.routers import DefaultRouter
from .views import ScrumModelViewSet,CreateInvitationView
from django.urls import include, path
from django.conf.urls import url

Router = DefaultRouter()


Router.register("",ScrumModelViewSet)

urlpatterns = [

    path('Scrum/', include(Router.urls)),
    url('invitations/', CreateInvitationView.as_view()),
    # url(r'^invitations/accept-invite/(?P<key>\w+)/?$', TaskListByState2.as_view(), name='accept-invite'),
    # url(r'^', include('rest_invitations.urls')),
    
]