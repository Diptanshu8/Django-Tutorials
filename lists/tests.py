from django.test import TestCase
from django.core.urlresolvers import resolve
from lists.views import home_page
from django.http import HttpRequest
from lists.models import Item
from django.template.loader import render_to_string 
# Create your tests here.
#class tempclass_homepagetest(TestCase):
#    def test_to_test_homepage(self):
#        found = resolve('/')
#        self.assertEqual(found.func,home_page)
#       def test_to_correct_response_by_template(self):
#        request = HttpRequest()
#        response = home_page(request)
#        expected_html = render_to_string('home.html')
#        self.assertEqual(response.content.decode(),expected_html)
#        def test_to_do_a_POST_request(self):
#            request = HttpRequest()
#            request.method = 'POST'
#            request.POST['item_text'] ='A new list item'
#            response = home_page(request)
#            #self.assertIn('A new list item',response.content.decode())
#            expected_html = render_to_string('home.html',{'new_item_text':'A new list item'})
#            self.assertEqual(expected_html,response.content.decode())
class ORMTesting(TestCase):
    def test_saving_and_retrieving_item(self):
        first_item = Item()
        first_item.text = "First(ever) list item"
        first_item.save()

        second_item = Item()
        second_item.text="second Item"
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(),2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text,"First(ever) list item")
        self.assertEqual(second_saved_item.text,"second Item")

