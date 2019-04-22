from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    url(r'^$', views.project_list, name="list"),
    url(r'^(?P<slug>[\w-]+)/$', views.project_detail, name="details"),
]
