from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'webapps.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

	url(r'^$','socialnetwork.views.home', name = 'home'),
	url(r'^post$','socialnetwork.views.post', name='post'),
	url(r'^login$','django.contrib.auth.views.login',{'template_name':'socialnetwork/login.html'},name='login'),
	url(r'^logout$', 'django.contrib.auth.views.logout_then_login',name='logout'),
	url(r'^register$','socialnetwork.views.register',name='register'),
	url(r'^profile/(?P<id>\w+)$','socialnetwork.views.userProfile',name='profile'),
	url(r'^edit/(?P<id>\d+)$','socialnetwork.views.editProfile',name='edit'),
	url(r'^comment/(\d+)$','socialnetwork.views.comment', name='comment'),
	url(r'^delete/(\d+)$','socialnetwork.views.delete', name='delete'),
	url(r'^get-posts$','socialnetwork.views.get_posts',name='get posts'),
	url(r'^myProfile$','socialnetwork.views.profile',name='myProfile'),
	url(r'^photo/(?P<id>\d+)$','socialnetwork.views.get_photo',name='photo'),
	# The following URL should match any username valid in Django and
    # any token produced by the default_token_generator
    url(r'^confirm-registration/(?P<username>[a-zA-Z0-9_@\+\-]+)/(?P<token>[a-z0-9\-]+)$', 'addrbook.views.confirm_registration', name='confirm'),	
)
