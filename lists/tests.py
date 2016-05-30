from django.test import TestCase
from django.core.urlresolvers import resolve
from lists.views import home_page
from django.http import HttpRequests 

# Create your tests here.
class tempclass_homepagetest(TestCase):
	def test_to_test_homepage(self):
		found = resolve('/')
		self.assertEqual(found.func,home_page)
	def test_to_httpresponse(self):
		request = HttpRequest()
		response = home_page(request)
		self.assertIn(b'<title>To-Do</title>',response.content)	
