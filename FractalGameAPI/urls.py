from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
  url(r'^insert/mandelbrot/', 'FractalGameAPI.views.insert_mandelbrot_route', name='insert_mandelbrot_route'),
  url(r'^generate/mandelbrot/(\d+)/$', 'FractalGameAPI.views.generate_mandelbrot_route', name='generate_mandelbrot_route'),
)
urlpatterns += staticfiles_urlpatterns()
