from django.conf.urls import patterns, include, url
from CrackItDemo.login import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    # Link that directs to the login/sign up page
    url(r'^$', views.login_page, name='login-page'),

    # Examples:
    # url(r'^$', 'CrackItDemo.views.home', name='home'),
    # url(r'^CrackItDemo/', include('CrackItDemo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
