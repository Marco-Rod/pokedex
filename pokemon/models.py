from django.db import models
from model_utils import Choices
from django.utils.translation import gettext as _

# Create your models here.

class Region(models.Model):
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=500)
	class Meta:
		verbose_name = "Region"
		verbose_name_plural = "Regions"
	def __str__(self):
		return self.name

class City(models.Model):
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=500)
	region = models.ForeignKey(Region, related_name = 'regions')

	class Meta:
		verbose_name = "City"
		verbose_name_plural = "Cities"

	def __str__(self):
		return self.name

class Town(models.Model):
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=500)
	city = models.ForeignKey(City, related_name= 'cities')

	class Meta:
		verbose_name = "Town"
		verbose_name_plural = "Towns"

	def __str__(self):
		return self.name

class Medal(models.Model):
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=500)
	image = models.FileField(upload_to='images/')

	class Meta:
		verbose_name = "Medal"
		verbose_name_plural = "Medals"

	def __str__(self):
		return name

class Move(models.Model):
	name = models.CharField(max_length=100)
	power = models.IntegerField()

	class Meta:
		verbose_name = "Move"
		verbose_name_plural = "Moves"

	def __str__(self):
		return self.name

class Type(models.Model):
	name = models.CharField(max_length=100)
	move = models.ManyToManyField(Move, related_name="Moves")

	class Meta:
		verbose_name = "Type"
		verbose_name_plural = "Types"

	def __str__(self):
		return self.name

class Lider(models.Model):
	name = models.CharField(max_length=100)
	types = models.ManyToManyField(Type, related_name="Types")
	class Meta:
		verbose_name = "Lider"
		verbose_name_plural = "Liders"

	def __str__(self):
		return self.name

class Gym(models.Model):    
	name = models.CharField(max_length=100)
	city = models.ForeignKey(City)
	medal = models.ForeignKey(Medal)
	lider = models.ForeignKey(Lider)

	class Meta:
		verbose_name = "Gym"
		verbose_name_plural = "Gyms"

	def __str__(self):
		return self.name

class Professor(models.Model):    	    
	name = models.CharField(max_length=100)    	
	region = models.ForeignKey(Region)
	home = models.CharField(max_length=200)
	specialty = models.CharField(max_length=100)

	class Meta:
		verbose_name = "Professor"
		verbose_name_plural = "Professors"

	def __str__(self):
		return self.name

class Species(models.Model):
	name = models.CharField(max_length=100)

	class Meta:
		verbose_name = "Species"
		verbose_name_plural = "Speciess"

	def __str__(self):
		self.name

class Generation(models.Model):    
	name = models.CharField(max_length=100)
	class Meta:
		verbose_name = "Generation"
		verbose_name_plural = "Generations"

	def __str__(self):
		self.name

class Ability(models.Model):
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=500)

	class Meta:
		verbose_name = "Ability"
		verbose_name_plural = "Abilities"

	def __str__(self):
		self.name

class Habitat(models.Model):    
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=500)

	class Meta:
		verbose_name = "Habitat"
		verbose_name_plural = "Habitats"

	def __str__(self):
		return self.name

class Pokemon(models.Model):
	
	GENDER = Choices(
		(0,'male', _('male')),
		(1,'female', _('female')))
	
	name = models.CharField(max_length=100)
	number = models.CharField(max_length=100)
	species = models.ForeignKey(Species)
	types = models.ManyToManyField(Type)
	initial = models.BooleanField()
	legendary = models.BooleanField()
	ability = models.ManyToManyField(Ability)
	weight = models.CharField(max_length=10)
	height = models.CharField(max_length=10)
	gender = models.IntegerField(choices=GENDER, default=GENDER.male)
	habitat = models.ForeignKey(Habitat)
	color = models.CharField(max_length=50)
	generation = models.ForeignKey(Generation)
	photo = models.FileField(upload_to='images/')
	
	class Meta:
		verbose_name = "Pokemon"
		verbose_name_plural = "Pokemons"

	def __str__(self):
		self.name