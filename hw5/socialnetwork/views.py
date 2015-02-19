from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist

# Decorator to use built-in authentication system
from django.contrib.auth.decorators import login_required

# Used to create and manually log in a user
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate

# Django transaction system so we can use @transaction.atomic
from django.db import transaction

from socialnetwork.models import *
from socialnetwork.forms import *

from datetime import datetime


@login_required
def home(request):
	posts = Post.objects.all()
	context = {'posts': posts, 'form': PostForm() }
	print context['posts']
	return render(request,'socialnetwork/index.html',context)

@login_required
@transaction.atomic	
def post(request):
	errors = []
	
	if request.method == 'GET':
		context = {'form': PostForm() }
		return render(request,'socialnetwork/index.html',context)
		
	new_post = Post(user=request.user,
				creation_time=datetime.now(),
				update_time=datetime.now())
	post_form = PostForm(request.POST, instance=new_post)
	if not post_form.is_valid():
		context = {'form': post_form }
		return render(request, 'socialnetwork/index.html',context)
		
	post_form.save()
		
	edit_form = EditForm(instance=new_post)	
	posts = Post.objects.all()
	context = {'posts' : posts, 'errors':errors, 'form':edit_form }
	return render(request, 'socialnetwork/index.html',context)

@login_required
def userProfile(request,id):

	posts = Post.objects.filter(user__username = id)
	context = {'posts' : posts,'user' : id}
	return render(request,'socialnetwork/profile.html',context)
	
@login_required
@transaction.atomic
def editProfile(request,id):
	errors = []
	try:
		if request.method == 'GET':
			post = Post.objects.get(id=id)
			form = EditForm(instance=post)
			context = { 'post':post, 'form': form }
			return render(request, 'socialnetwork/edit.html', context)	
		
		post = Post.objects.get(id=id)
		dp_update_time = entry.update_time
		form = EditForm(request.POST, instance=entry)
		if not form.is_valid():
			context = {'entry': entry, 'form': form}
			return render(request, 'socialnetwork/edit.html', context)
			
		if db_update_time != form.cleaned_data['update_time']:
			post = Post.objects.get(id=id)
			form = EditForm(instance=post)
			errors.append('Post already modified')
			context = { 'post': post,
						'form': form,
						'errors': errors,
						}
			return render(request, 'socialnetwork/edit.html',context)
			
		entry.update_time = datetime.now()
		form.save()
		
		context = {
			'post': post,
			'form': form,
			'errors': errors,
		}
		return render(request, 'socialnetwork/edit.html',context)
	except Post.DoesNotExist:
		errors.append('Post with id={0} does not exist'.format(id) )
		context = {'errors': errors}
		return render(request, 'socialnetwork/index.html',context)
	
@transaction.atomic
def register(request):
    context = {}

    # Just display the registration form if this is a GET request.
    if request.method == 'GET':
        context['form'] = RegistrationForm()
        return render(request, 'socialnetwork/register.html', context)

    # Creates a bound form from the request POST parameters and makes the 
    # form available in the request context dictionary.
    form = RegistrationForm(request.POST)
    context['form'] = form

    # Validates the form.
    if not form.is_valid():
        return render(request, 'socialnetwork/register.html', context)

    # At this point, the form data is valid.  Register and login the user.
    new_user = User.objects.create_user(username=form.cleaned_data['username'], 
                                        password=form.cleaned_data['password1'],
                                        first_name=form.cleaned_data['first_name'],
                                        last_name=form.cleaned_data['last_name'])
    new_user.save()

    # Logs in the new user and redirects to his/her todo list
    new_user = authenticate(username=form.cleaned_data['username'],
                            password=form.cleaned_data['password1'])
    login(request, new_user)
    return redirect(reverse('home'))
	
	
