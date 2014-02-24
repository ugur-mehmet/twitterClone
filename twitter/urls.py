from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'twitterClone.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^index$','views.index', name='home'),
    url(r'^login$','views.login'),
    url(r'^logout$','views.logout'),
    url(r'^signup$','views.signup'),
)
