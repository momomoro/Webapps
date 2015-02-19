from django.db import models
from django.utils import timezone
from datetime import *

# User class for built-in authentication module
from django.contrib.auth.models import User

# Data model for a socialnetwork post
class Post(models.Model):
	text = models.CharField(max_length=160)
	user = models.ForeignKey(User)
	creation_time = models.DateTimeField(auto_now_add=True)
	update_time = models.DateTimeField()
	
	def __unicode__(self):
		return 'user=' + str(self.user) + ',text="'+ self.text + '" time='+ str(self.creation_time)
