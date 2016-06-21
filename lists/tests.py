from django.test import TestCase
from django.core.urlresolvers import resolve
from lists.views import home_page
from django.http import HttpRequest
from django.template.loader import render_to_string 
# Create your tests here.
class tempclass_homepagetest(TestCase):
	def test_to_test_homepage(self):
		found = resolve('/')
		self.assertEqual(found.func,home_page)
	def test_to_correct_response_by_template(self):
		request = HttpRequest()
		response = home_page(request)
		expected_html = render_to_string('home.html')
		self.assertEqual(response.content.decode(),expected_html)
	def test_to_do_a_POST_request(self):
		request = HttpRequest()
		request.method = 'POST'
		request.POST['item_text'] ='A temp list item'
		response = home_page(request)
		self.assertIn('A temp list item',response.content.decode())
