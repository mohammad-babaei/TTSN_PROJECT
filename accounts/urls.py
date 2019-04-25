from django.conf.urls import url,include
from .views import UserCreateAPIView,UserLoginAPIView
from . import views
from rest_framework_jwt.views import obtain_jwt_token,refresh_jwt_token
from allauth.account.views import ConfirmEmailView


urlpatterns = [
    url(r'^register/$',UserCreateAPIView.as_view(),name = 'register'),
    url(r'^login/$',UserLoginAPIView.as_view(),name = 'login'),
    url(r'login/token-auth', obtain_jwt_token),
    url(r'login/token-refresh', refresh_jwt_token),
    
    url(r'^registration/account-email-verification-sent/', views.null_view, name='account_email_verification_sent'),
    url(r'^registration/account-confirm-email/(?P<key>[-:\w]+)/$', ConfirmEmailView.as_view(), name='account_confirm_email'),
    url(r'^registration/complete/$', views.complete_view, name='account_confirm_complete'),
    url(r'^password-reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.null_view, name='password_reset_confirm'),
    # Default urls
    # url(r'', include('rest_auth.urls')),
    url(r'^registration/', include('rest_auth.registration.urls')),

]


"""
curl -X POST -d "username=admin&password=bahar1393" http://localhost:8000/accounts/login/token-auth/


curl -H "Authorization: JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjo0LCJleHAiOjE1NTYxMzI0NDAsInVzZXJuYW1lIjoiYWRtaW4iLCJlbWFpbCI6Im1hbWFseTExNTVAZ21haS5jb20ifQ.sSoNM6LuG39Ylv8xm2Bu9OUrIpguZIfqi6v0Oy_5uO4" http://localhost:8000/accounts/register/


"""


"""

how to send registeration request to get verification email



curl -H "Content-Type: application/json" -X POST -d '{"username":"someusername","email":"mr.linux3@yahoo.com","password1":"bahar1393","password2":"bahar1393"}' http://localhost:8000/auth/registration/


"""