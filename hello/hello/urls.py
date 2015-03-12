from django.conf.urls import *
from django.contrib import admin
from hello.view import hello,homepage

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hello.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

	url(r'^hello/$',hello),
	url(r'^$',homepage),

)
