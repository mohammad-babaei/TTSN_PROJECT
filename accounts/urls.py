from django.conf.urls import url
from .views import UserCreateAPIView,UserLoginAPIView
from rest_framework_jwt.views import obtain_jwt_token,refresh_jwt_token


urlpatterns = [
    url(r'^register/$',UserCreateAPIView.as_view(),name = 'register'),
    url(r'^login/$',UserLoginAPIView.as_view(),name = 'login'),
    url(r'login/token-auth', obtain_jwt_token),
    url(r'login/token-refresh', refresh_jwt_token),

]


"""
curl -X POST -d "username=admin&password=bahar1393" http://localhost:8000/accounts/login/token-auth/


curl -H "Authorization: JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjo0LCJleHAiOjE1NTYxMzI0NDAsInVzZXJuYW1lIjoiYWRtaW4iLCJlbWFpbCI6Im1hbWFseTExNTVAZ21haS5jb20ifQ.sSoNM6LuG39Ylv8xm2Bu9OUrIpguZIfqi6v0Oy_5uO4" http://localhost:8000/accounts/register/


"""