from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
  url(r'^insert/mandelbrot/', 'FractalGuesserAPI.views.insert_mandelbrot_route', name='insert_mandelbrot_route'),
  url(r'^generate/mandelbrot/(\d+)/$', 'FractalGuesserAPI.views.generate_mandelbrot_route', name='generate_mandelbrot_route'),
)
urlpatterns += staticfiles_urlpatterns()
