from sys import stderr
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import TestCase
from json import loads, dumps

from FractalGuesserAPI.views import generate_mandelbrot_route, ROUTE_COUNT
from FractalGuesserAPI.models import MandelbrotRoute

class RouteBuilder(TestCase):
  def test_insert_level_one(self):
    self.client.post('/api/insert/mandelbrot/', {'level': 1, 'route': '[{0,0}]', 'route_id': 1})
    self.assertEqual(MandelbrotRoute.objects.count(), 1)
    route = MandelbrotRoute.objects.get(pk=1)
    self.assertEqual(route.level, 1)
    self.assertEqual(route.route, '[{0,0}]')

# note there are some inadmissible routes, so insertion must be done manually
def insert_level_one_routes(self):
  self.client.post('/api/insert/mandelbrot/', {'level': 1, 'route': '[{"x": 0,"y": 1}]', 'route_id': 1})
  self.client.post('/api/insert/mandelbrot/', {'level': 1, 'route': '[{"x": 0,"y": 2}]', 'route_id': 2})
  self.client.post('/api/insert/mandelbrot/', {'level': 1, 'route': '[{"x": 1,"y": 0}]', 'route_id': 3})
  self.client.post('/api/insert/mandelbrot/', {'level': 1, 'route': '[{"x": 1,"y": 1}]', 'route_id': 4})
  self.client.post('/api/insert/mandelbrot/', {'level': 1, 'route': '[{"x": 1,"y": 2}]', 'route_id': 5})
  self.client.post('/api/insert/mandelbrot/', {'level': 1, 'route': '[{"x": 1,"y": 3}]', 'route_id': 6})
  self.client.post('/api/insert/mandelbrot/', {'level': 1, 'route': '[{"x": 2,"y": 0}]', 'route_id': 7})
  self.client.post('/api/insert/mandelbrot/', {'level': 1, 'route': '[{"x": 2,"y": 1}]', 'route_id': 8})
  self.client.post('/api/insert/mandelbrot/', {'level': 1, 'route': '[{"x": 2,"y": 2}]', 'route_id': 9})
  self.client.post('/api/insert/mandelbrot/', {'level': 1, 'route': '[{"x": 2,"y": 3}]', 'route_id': 10})
  self.client.post('/api/insert/mandelbrot/', {'level': 1, 'route': '[{"x": 3,"y": 0}]', 'route_id': 11})
  self.client.post('/api/insert/mandelbrot/', {'level': 1, 'route': '[{"x": 3,"y": 1}]', 'route_id': 12})
  self.client.post('/api/insert/mandelbrot/', {'level': 1, 'route': '[{"x": 3,"y": 2}]', 'route_id': 13})
  self.client.post('/api/insert/mandelbrot/', {'level': 1, 'route': '[{"x": 3,"y": 3}]', 'route_id': 14})

class RouteGenerator(TestCase):
  def test_single_level_one_loads(self):
    insert_level_one_routes(self)
    response = self.client.get('/api/generate/mandelbrot/1/')
    data = loads(response.content.decode("utf-8"))
    self.assertEqual(data['level'], 1)
    self.assertEqual(len(data['route']), 1)
    
  def test_multiple_level_one_returns_different_routes(self):
    insert_level_one_routes(self)
    response1 = self.client.get('/api/generate/mandelbrot/1/')
    data1 = loads(response1.content.decode("utf-8"))
    response2 = self.client.get('/api/generate/mandelbrot/1/')
    data2 = loads(response2.content.decode("utf-8"))
    self.assertFalse(data1['route'][0]['x'] == data2['route'][0]['x'] and data1['route'][0]['y'] == data2['route'][0]['y'])
  
  def test_returns_route_level(self):
    insert_level_one_routes(self)
    response = self.client.get('/api/generate/mandelbrot/1/')
    decoded_response = loads(response.content.decode("utf-8"))
    self.assertEqual(len(decoded_response['route']), decoded_response['level'])
