from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
  url(r'^mandelbrot/', 'FractalGuesserWebsite.views.mandelbrot', name='mandelbrot'),
  url(r'^juliet/', 'FractalGuesserWebsite.views.juliet', name='juliet'),
)
urlpatterns += staticfiles_urlpatterns()
