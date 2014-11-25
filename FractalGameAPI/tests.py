from sys import stderr
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import TestCase

from FractalGameAPI.views import generate_route
from FractalGameAPI.models import Route

class RouteBuilder(TestCase):
  def test_insert_level_one(self):
    self.client.post('/api/insert/', {'level': 1, 'route': '[{1,1}]'})
    self.assertEqual(Route.objects.count(), 1)
    route = Route.objects.get(pk=1)
    self.assertEqual(route.level, 1)
    self.assertEqual(route.route, '[{1,1}]')

def insert_level_one_routes(self):
  self.client.post('/api/insert/', {'level': 1, 'route': '[{0,1}]'})
  self.client.post('/api/insert/', {'level': 1, 'route': '[{0,2}]'})
  self.client.post('/api/insert/', {'level': 1, 'route': '[{1,0}]'})
  self.client.post('/api/insert/', {'level': 1, 'route': '[{1,1}]'})
  self.client.post('/api/insert/', {'level': 1, 'route': '[{1,2}]'})
  self.client.post('/api/insert/', {'level': 1, 'route': '[{1,3}]'})
  self.client.post('/api/insert/', {'level': 1, 'route': '[{2,0}]'})
  self.client.post('/api/insert/', {'level': 1, 'route': '[{2,1}]'})
  self.client.post('/api/insert/', {'level': 1, 'route': '[{2,2}]'})
  self.client.post('/api/insert/', {'level': 1, 'route': '[{2,3}]'})
  self.client.post('/api/insert/', {'level': 1, 'route': '[{3,0}]'})
  self.client.post('/api/insert/', {'level': 1, 'route': '[{3,1}]'})
  self.client.post('/api/insert/', {'level': 1, 'route': '[{3,2}]'})
  self.client.post('/api/insert/', {'level': 1, 'route': '[{3,3}]'})

class RouteGenerator(TestCase):
  def test_single_level_one(self):
    insert_level_one_routes(self)
    response = self.client.get('/api/generate/1/')
    self.assertEqual(len(response.content.decode("utf-8")), 9)
    
  def test_multiple_level_one_returns_different_routes(self):
    insert_level_one_routes(self)
    response1 = self.client.get('/api/generate/1/')
    response2 = self.client.get('/api/generate/1/')
    self.assertNotEqual(response1.content, response2.content)
    
  def test_level_one_and_two_returns_different_route_length(self):
    insert_level_one_routes(self)
    response1 = self.client.get('/api/generate/1/')
    response2 = self.client.get('/api/generate/2/')
    self.assertNotEqual(len(response1.content.decode("utf-8")), len(response2.content.decode("utf-8")))
