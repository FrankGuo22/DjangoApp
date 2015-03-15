from django.conf.urls import *
from django.contrib import admin
from hello.view import hello,homepage
from books.views import search_form,search
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hello.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^admin/',include(admin.site.urls)),
	url(r'^hello/$',hello),
	url(r'^$',homepage),
	url(r'^search_form/$',search_form),
	url(r'^search/$',search),

)
