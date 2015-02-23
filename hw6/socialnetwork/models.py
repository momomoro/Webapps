from django.db import models
from django.utils import timezone
from django.contrib.auth.models import *
from django.db.models.signals import post_save

from datetime import *

# User class for built-in authentication module
from django.contrib.auth.models import User

class Blogger(models.Model):
	user = models.OneToOneField(User, primary_key=True)
	following = models.ManyToManyField(User, symmetrical = False,blank=True, related_name="followers")
	picture = models.FileField(upload_to="pictures",blank=True)
	
	def __unicode__(self):
		return 'user=' + str(self.user)
		

# Data model for a socialnetwork post
class Post(models.Model):
	text = models.CharField(max_length=160)
	user = models.ForeignKey(User)
	creation_time = models.DateTimeField(auto_now_add=True)
	update_time = models.DateTimeField()
	
	def __unicode__(self):
		return 'id=' + str(self.id) + 'user=' + str(self.user) + ',text="'+ self.text + '" time='+ str(self.creation_time)
		

