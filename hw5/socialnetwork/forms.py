from django import forms

from django.contrib.auth.models import User
from models import *

class RegistrationForm(forms.Form):
	first_name = forms.CharField(max_length=20)
	last_name = forms.CharField(max_length=20)
	username = forms.CharField(max_length=20)
	password1 = forms.CharField(max_length = 20,
								label='Password',
								widget = forms.PasswordInput())
	password2 = forms.CharField(max_length = 20,
								label='Confirm password',
								widget = forms.PasswordInput())
	image = forms.FileField(upload_to="pictures",blank = True)
								
	def clean(self):
	
		cleaned_data = super(RegistrationForm, self).clean()
		
		password1 = cleaned_data.get('password1')
		password2 = cleaned_data.get('password2')
		if password1 and password2 and password1 != password2:
			raise forms.ValidationError("Passwords did not match.")
			
		return cleaned_data
		
	def clean_username(self):
		username = self.cleaned_data.get('username')
		if User.objects.filter(username__exact=username):
			raise forms.ValidationError("Username is already taken.")
			
		return username
	
	def clean_image(self):
		image = self.cleaned_data['image']
		if not image:
			return None
		if not image.content_type or image.content_type.startswith('image'):
			raise forms.ValidationError("File type is not an image")
		return picture
		
class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		exclude = (
			'user',
			'creation_time',
			'update_time',
		)
		
class EditForm(forms.ModelForm):
	class Meta:
		model = Post
		exclude = (
			'user',
			'creation_time',
		)
		widgets = {
			'update_time': forms.HiddenInput,
		}