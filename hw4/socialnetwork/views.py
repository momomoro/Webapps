from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist

# Decorator to use built-in authentication system
from django.contrib.auth.decorators import login_required

# Used to create and manually log in a user
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate

# Django transaction system so we can use @transaction.atomic
from django.db import transaction

from socialnetwork.models import *

import datetime


@login_required
def home(request):
	posts = Post.objects.all()
	return render(request,'socialnetwork/index.html',{'posts': posts})

@login_required
@transaction.atomic	
def post(request):
	errors = []
	
	print request.POST
	
	if 'post' not in request.POST or not request.POST['post']:
		errors.append('You must enter a post.')
	else:
		new_post = Post(text=request.POST['post'], user=request.user)
		new_post.save()
		
	posts = Post.objects.all()
	context = {'posts' : posts, 'errors':errors}
	return render(request, 'socialnetwork/index.html',context)

@login_required
def userProfile(request,id):

	print request.user
	print id
	posts = Post.objects.filter(user = id)
	context = {'posts' : posts,'user' : user_id}
	return render(request,'socialnetwork/profile.html',context)
	
@transaction.atomic
def register(request):
    context = {}

    # Just display the registration form if this is a GET request
    if request.method == 'GET':
        return render(request, 'socialnetwork/register.html', context)

    errors = []
    context['errors'] = errors

    # Checks the validity of the form data
    if not 'username' in request.POST or not request.POST['username']:
    	errors.append('Username is required.')
    else:
        # Save the username in the request context to re-fill the username
        # field in case the form has errrors
        context['username'] = request.POST['username']

    if not 'password1' in request.POST or not request.POST['password1']:
        errors.append('Password is required.')
    if not 'password2' in request.POST or not request.POST['password2']:
        errors.append('Confirm password is required.')

    if 'password1' in request.POST and 'password2' in request.POST \
            and request.POST['password1'] and request.POST['password2'] \
            and request.POST['password1'] != request.POST['password2']:
        errors.append('Passwords did not match.')

    if len(User.objects.filter(username = request.POST['username'])) > 0:
        errors.append('Username is already taken.')

    if errors:
        return render(request, 'socialnetwork/register.html', context)

    # Creates the new user from the valid form data
    new_user = User.objects.create_user(username=request.POST['username'], \
                                        password=request.POST['password1'])
    new_user.save()

    # Logs in the new user and redirects to his/her todo list
    new_user = authenticate(username=request.POST['username'], \
                            password=request.POST['password1'])
    login(request, new_user)
    return redirect('/socialnetwork/')
	
	
