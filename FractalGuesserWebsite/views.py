from django.shortcuts import render, redirect
from django.http import HttpResponse

def home_page(request):
	return render(request, 'home.html')	
	
def china_home_page(request):
	return render(request, 'china_home.html')
	
def juliet(request):
	return render(request, 'juliet.html')
	
def mandelbrot(request):
	return render(request, 'mandelbrot.html')
	
def generate_routes(request):
  return render(request, 'generate_routes.html')
