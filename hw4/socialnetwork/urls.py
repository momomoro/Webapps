from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'webapps.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	url(r'^$','socialnetwork.views.home'),
	url(r'^post','socialnetwork.views.post'),
	url(r'^login$','django.contrib.auth.views.login',{'template_name':'socialnetwork/login.html'}),
	url(r'^logout$', 'django.contrib.auth.views.logout_then_login'),
	url(r'^register$','socialnetwork.views.register'),
	url(r'^profile/(?P<id>)','socialnetwork.views.userProfile'),

	
)
