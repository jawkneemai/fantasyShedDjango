import datetime

from django.db import models
from django.utils import timezone

'''
Making model changes:

Change your models (in models.py).
Run py manage.py makemigrations to create migrations for those changes
Run py manage.py sqlmigrate appname 000x to optionally check for SQL commands.
Run py manage.py migrate to apply those changes to the database.

'''

class Recipe(models.Model): 
	# Metadata
	name = models.CharField(max_length=100)
	pub_date = models.DateTimeField('Date Article Published')
	category = models.CharField(max_length=20)
	search_tags = models.CharField(max_length=1000)
	# Amazon S3 link for photos?

	# Ingredients, Recipe instructions
	ingredients = models.CharField(max_length=1000)
	instructions = models.CharField(max_length=10000)

	def __str__():
		return self.name

	'''
	or alternatively use ForeignKeys?

	def listCompile:
		ingredients_text = ''
		for ingredient in self.ingredients_list:
			ingredients_text += ingredient + ','
		return ingredients_text
	'''

class Question(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')

	def __str__(self):
		return self.question_text

	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

	def __str__(self):
		return self.choice_text
