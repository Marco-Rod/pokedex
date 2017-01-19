from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from apis import views


urlpatterns = [	
	url(r'^regions/$',views.RegionView.as_view(), name='region-list'),
	url(r'^regions/(?P<pk>[0-9]+)/$',views.RegionView.as_view(), name='region-create'),
]
urlpatterns = format_suffix_patterns(urlpatterns)