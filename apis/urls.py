from django.conf.urls import url, include
from rest_framework import routers
from apis import views


urlpatterns = [
	url(r'^', include(router.urls)),
]