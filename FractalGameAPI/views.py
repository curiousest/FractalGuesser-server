from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from FractalGameAPI.models import MandelbrotRoute
import random

MANDELBROT_ROUTE_LEVEL_RANGES = [1, 13, 81, 460]
	
def insert_mandelbrot_route(request):
  route = MandelbrotRoute()
  route.id = request.POST['route_id']
  route.level = request.POST['level']
  route.route = request.POST['route']
  route.save()
  return HttpResponse(route)
  
def generate_mandelbrot_route(request, level):
  count = MandelbrotRoute.objects.all().count()
  rand_id = random.randint(ROUTE_LEVEL_RANGES[int(level) - 1], MANDELBROT_ROUTE_LEVEL_RANGES[int(level)])
  route = MandelbrotRoute.objects.filter(id=rand_id)[0]
  return JsonResponse(route.route, safe=False)
