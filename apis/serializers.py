from django.contrib.auth.models import User, Group
from rest_framework import serializers
from pokemon.models import Region

class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ('url','username','email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Group
		fields = ('url', 'name')
			

class RegionSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Region
		fields = ('name','description')