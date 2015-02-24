from django.shortcuts import render, redirect, get_object_or_404
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
	posts = Post.objects.order_by('-creation_time')
	context = {'posts': posts, 'form': PostForm(), 'comment': CommentForm() }
	print context['posts']
	return render(request,'socialnetwork/index.html',context)

@login_required
def delete(request, id):
	context = {}
	if request.method != 'POST':
		return render(request,'socialnetwork/index.html')
	
	try:
		post = Post.objects.get(id=id)
		if post.user != request.user:
			message = "You can only delete your own posts"
			posts = posts = Post.objects.order_by('-creation_time')
			context = {'message': message,'posts': posts, 'form': PostForm() }
			return render(request,'socialnetwork/index.html',context)		
		post.delete()
	except ObjectDoesNotExist:
		message = "Post does not exist"
	return redirect('socialnetwork/index.html')

@login_required
@transaction.atomic
def comment(request,id):
	if request.method == 'GET':
		context = {'form' : CommentForm() }
		return render(request,'socialnetwork/index.html',context)
	
	post = Post.objects.get(id = id)
	new_comment = Comment(user=request.user,
				creation_time=datetime.now(),
				update_time=datetime.now())
	comment_form = CommentForm(request.POST, instance=new_comment)
	if not comment_form.is_valid():
		posts = Post.objects.order_by('-creation_time')
		context = {'form': post_form,'posts' : posts}
		return render(request, 'socialnetwork/index.html',context)
	
	comment_form.save()
	post.comments.add(new_comment)
	posts = Post.objects.order_by('-creation_time')
	context = {'posts' : posts, 'form':PostForm(), 'comment':CommentForm() }
	return redirect('socialnetwork/index.html')
	
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
		posts = Post.objects.order_by('-creation_time')
		context = {'form': post_form,'posts' : posts}
		return render(request, 'socialnetwork/index.html',context)
		
	post_form.save()
			
	posts = Post.objects.order_by('-creation_time')
	context = {'posts' : posts, 'errors':errors, 'form':PostForm() }
	return redirect('socialnetwork/index.html')

@login_required
def userProfile(request,id):
	context = {}
	try:
		User.objects.get(username = str(id))
		posts = Post.objects.filter(user__username = id).order_by('-creation_time')
		context = {'posts' : posts,'user' : id}
	except User.DoesNotExist:
		context = {'message' : 'User does not exist'}
	return render(request,'socialnetwork/profile.html',context)

@login_required
def profile(request):
	form = ProfileForm(instance = request.user)
	posts = Post.objects.filter(user__username = request.user).order_by('-creation_time')
	context = {'posts': posts,'profile': profile, 'form': form } 
	return render(request,'socialnetwork/myProfile.html',context)
	
@login_required
@transaction.atomic
def editProfile(request,id):
	errors = []
	try:	
		if request.method == 'GET':
			profile = User.objects.get(id = id)
			form = ProfileForm(instance=profile)
			context = { 'profile': profile, 'form': form }
			return render(request, 'socialnetwork/edit.html', context)
			
		profile = User.objects.get(id = id)
		form = ProfileForm(request.POST, instance=profile)
		if not form.is_valid():
			context = {'profile': profile, 'form': form}
			return render(request, 'socialnetwork/edit.html', context)
			
		form.save()
		
		context = {
			'profile': profile,
			'form': form,
			'errors': errors,
		}
		
		return render(request, 'socialnetwork/edit.html',context)
	except Post.DoesNotExist:
		errors.append('Profile with id={0} does not exist'.format(id) )
		context = {'errors': errors}
		return render(request, 'socialnetwork/index.html',context)

def get_posts(request):
	reponse_text = serializers.serialize('json',Posts.objects.all())
	return HttpResponse(response_text, content_type='application/json')
		
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
	
	new_blogger = Blogger(user=new_user)
	new_blogger.save()
		
    # Logs in the new user and redirects to his/her todo list
	new_user = authenticate(username=form.cleaned_data['username'],
							password=form.cleaned_data['password1'])
	login(request, new_user)
	return redirect(reverse('home'))
	
	
