from django.test import TestCase
from django.core.urlresolvers import resolve
from lists.views import home_page
from django.http import HttpRequest
from lists.models import Item
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
            #self.assertEqual(response.content.decode(),expected_html)
        def test_to_check_homepage_saves_POST_request(self):
            request = HttpRequest()
            request.method = 'POST'
            request.POST['item_text'] ='A new list item'
            response = home_page(request)
            self.assertEqual(Item.objects.count(),1)
            new_item=Item.objects.first()
            self.assertEqual(new_item.text,'A new list item')
        def test_to_check_that_POST_request_is_redirected(self):
            request = HttpRequest()
            request.method = 'POST'
            request.POST['item_text'] ='A new list item'
            response = home_page(request)
            self.assertEqual(response.status_code,302)
            self.assertEqual(response['location'],'/')
        def test_to_check_display_of_multiple_entries(self):
            Item.objects.create(text='entry 1')
            Item.objects.create(text='entry 2')
            request = HttpRequest()
            response = home_page(request)
            self.assertIn('entry 1',response.content.decode())
            self.assertIn('entry 2',response.content.decode())
            
            

"""
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
"""
