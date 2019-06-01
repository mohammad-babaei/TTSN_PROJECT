from django.conf.urls import url
from Backlog import views

urlpatterns = [
    url(r'^',views.BacklogList.as_view()),
]

