from django.test import TestCase
from django.core.urlresolvers import resolve
from lists.views import home_page

# Create your tests here.
class tempclass_homepagetest(TestCase):
	def test_to_test_homepage(self):
		found = resolve('/')
		self.assertEqual(found.func,home_page)
