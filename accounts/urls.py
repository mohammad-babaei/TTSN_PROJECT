from django.conf.urls import url,include

from django import urls
from .views import UserCreateAPIView,UserLoginAPIView,ViewCurrentUserInfo,ViewCurrentUserProjects
from . import views
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token,refresh_jwt_token
from allauth.account.views import ConfirmEmailView



router = routers.DefaultRouter()

router.register('userview',views.UserView)


urlpatterns = [
    # url(r'^register/$',UserCreateAPIView.as_view(),name = 'register'),
    # url(r'^login/$',UserLoginAPIView.as_view(),name = 'login'),
    url(r'login/token-auth', obtain_jwt_token),
    # url(r'users', views.UserView),
    url(r'login/token-refresh', refresh_jwt_token),
    # url(r'userview/', views.UserView.as_view(({'get': 'list'})),name='user-details'),

    urls.path('',urls.include(router.urls)),
    url(r'^current_user/$', ViewCurrentUserInfo.as_view(), name='view_current_user_info'),
    url(r'^Projects/$', ViewCurrentUserProjects.as_view(), name='view_current_user_projects'),
    url(r'^registration/account-email-verification-sent/', views.null_view, name='account_email_verification_sent'),
    url(r'^registration/account-confirm-email/(?P<key>[-:\w]+)/$', ConfirmEmailView.as_view(), name='account_confirm_email'),
    url(r'^registration/complete/$', views.complete_view, name='account_confirm_complete'),
    url(r'^password-reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.null_view, name='password_reset_confirm'),
    # Default urls
    # url(r'', include('rest_auth.urls')),
    url(r'^registration/', include('rest_auth.registration.urls')),

]

