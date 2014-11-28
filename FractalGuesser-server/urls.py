from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'FractalGame.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'FractalGuesserWebsite.views.home_page', name='home'),
    url(r'^generate_routes/', 'FractalGuesserWebsite.views.generate_routes', name='generate_routes'),
    url(r'^api/', include('FractalGuesserAPI.urls')),
)
