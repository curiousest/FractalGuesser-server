from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from FractalGuesserAPI.models import MandelbrotRoute
from json import loads
import random

MANDELBROT_ROUTE_LEVEL_RANGES = [1, 13, 81, 460]
ROUTE_COUNT = MandelbrotRoute.objects.all().count()
	
def insert_mandelbrot_route(request):
  route = MandelbrotRoute()
  route.id = request.POST['route_id']
  route.level = request.POST['level']
  route.route = request.POST['route']
  route.save()
  return HttpResponse(route)

def generate_mandelbrot_route(request, level):
  if (level is not None):
    rand_id = random.randint(MANDELBROT_ROUTE_LEVEL_RANGES[int(level) - 1], MANDELBROT_ROUTE_LEVEL_RANGES[int(level)])
  else:
    rand_id = random.randint(1, ROUTE_COUNT - 1)
  route = MandelbrotRoute.objects.filter(id=rand_id)[0]
  response_object = {"level": route.level, "route": loads(route.route)}
  return JsonResponse(response_object, safe=False)
  
def generate_mandelbrot_route_random(request):
  return generate_mandelbrot_route(request, None)
