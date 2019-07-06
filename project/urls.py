from rest_framework.routers import DefaultRouter
from .views import ScrumModelViewSet,CreateInvitationView,UpdateInvitationView,ViewCollaborators
from django.urls import include, path
from django.conf.urls import url

Router = DefaultRouter()


Router.register("",ScrumModelViewSet)

urlpatterns = [

    path('Scrum/', include(Router.urls)),
    
    url(r'collaborators/(?P<project_id>.+)/$', ViewCollaborators.as_view()),
    url(r'invitations/$', CreateInvitationView.as_view()),
    url(r'^invitations/accept-invite/(?P<key>\w+)/?$', UpdateInvitationView.as_view(), name='accept-invite'),
    # url(r'^', include('rest_invitations.urls')),
    
]