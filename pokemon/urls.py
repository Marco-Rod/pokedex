from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^elloworld/$', views.index, name='index'),
]