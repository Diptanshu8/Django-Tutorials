from django.test import TestCase

# Create your tests here.
class tempclass(TestCase):
	def test_first(self):
		self.assertEqual(1+1,3)
