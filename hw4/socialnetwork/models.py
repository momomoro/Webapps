from django.db import models

# User class for built-in authentication module
from django.contrib.auth.models import User

# Data model for a socialnetwork post
class Post(models.Model):
	text = models.CharField(max_length=160)
	user = models.ForeignKey(User)
	time = models.DateTimeField(auto_now=True,auto_now_add=True)
	
	def __unicode__(self):
		return 'id=' + str(self.id) + ',text="'+ self.text + '" time='+ str(self.time)
