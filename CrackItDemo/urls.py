# This code and all its derivatives exclusively belongs to crackit inc
# Copyright 2013 crackit, Inc. - All Rights Reserved
# Author: Kwadwo Nyarko, Perry Ogwuche - 8-21-2-2013

from django.conf.urls import patterns, include, url
from CrackItDemo.registration import views as registration_views
from CrackItDemo.video import views as video_views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # User login
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),

    # This URL directs you to the login/signup page
    url(r'^$', registration_views.login_page, name='login-page'),
    url(r'^register', registration_views.register, name='register'),
	url(r'^video', video_views.video_page, name='video-page'),

    # Examples:
    # url(r'^$', 'CrackItDemo.views.home', name='home'),
    # url(r'^CrackItDemo/', include('CrackItDemo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
