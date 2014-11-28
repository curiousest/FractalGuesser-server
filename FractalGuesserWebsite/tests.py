from sys import stderr
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import TestCase

from FractalGuesserWebsite.views import home_page

def resolves_to_view(self, url, view):
	found = resolve(url)
	self.assertEqual(found.func, view)
	
def returns_correct_html(self, template, view):
	request = HttpRequest()
	response = view(request)
	expected_html = render_to_string(template)
	self.assertEqual(response.content.decode(), expected_html)

class AllPagesTest(TestCase):
	ALL_PAGES_DEF = [
		{'url': '/', 'template': 'home.html', 'view': home_page},
	]
	
	def test_static_pages_resolve(self):
		for page in self.ALL_PAGES_DEF:
			resolves_to_view(self, page['url'], page['view'])
	
	def test_static_pages_return_correct_html(self):
		for page in self.ALL_PAGES_DEF:
			returns_correct_html(self, page['template'], page['view'])
