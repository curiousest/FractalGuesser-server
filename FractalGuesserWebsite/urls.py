from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
  url(r'^mandelbrot/', 'FractalGuesserWebsite.views.mandelbrot', name='mandelbrot'),
  url(r'^juliet/', 'FractalGuesserWebsite.views.juliet', name='juliet'),
  url(r'^chinahome/', 'FractalGuesserWebsite.views.china_home_page', name='china_home_page'),
)
urlpatterns += staticfiles_urlpatterns()
