from django.shortcuts import render, redirect
from django.http import HttpResponse

def home_page(request):
	return render(request, 'home.html')
	
def generate_routes(request):
  return render(request, 'generate_routes.html')