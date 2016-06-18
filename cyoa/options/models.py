from django.db import models
# Create your models here.

class Section(models.Model):
	description = models.TextField(null=True)
	field_char = models.CharField(max_length = 40)
	number_in_set = models.IntegerField(default = 0)
	def __str__(self):
		return self.field_char

class Content(models.Model):
	description = models.CharField(max_length = 40, default = "Short description of content")
	section = models.ForeignKey(Section, on_delete=models.CASCADE)
	field_text = models.TextField()
	Image_ref = models.CharField(max_length = 400)
	def __str__(self):
		return self.description
		
class Intro(models.Model):
	title = models.CharField(max_length = 200, default = "new cyoa")
	number_in_set = models.IntegerField(default = 0)
	description = models.TextField()
	def __str__(self):
		return self.title