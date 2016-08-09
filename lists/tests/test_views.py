from django.test import TestCase
from django.core.urlresolvers import resolve
from lists.views import home_page
from django.http import HttpRequest
from lists.models import Item,List
from unittest import skip
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
        def test_to_check_that_POST_request_is_redirected(self):
            response = self.client.post('/lists/new',data={'item_text':'A new list item'})
            new_list=List.objects.first()
            self.assertRedirects(response,'/lists/%d/'%(new_list.id))
        def test_to_check_display_of_multiple_entries(self):
            list_ = List.objects.create()
            Item.objects.create(text='entry 1',list = list_)
            Item.objects.create(text='entry 2',list=list_)
            request = HttpRequest()
            response = home_page(request)
            #self.assertIn('entry 1',str(response.content.decode()))
            #self.assertIn('entry 2',(response.content.decode()))
class ListViewTestClass(TestCase):
    def test_using_the_list_template(self):
        list_ = List.objects.create()
        response = self.client.get('/lists/%d/'%(list_.id))
        self.assertTemplateUsed(response,'list.html')
    def test_displays_only_items_for_that_list(self):
        correct_list = List.objects.create()
        Item.objects.create(text='Entry 1',list = correct_list)
        Item.objects.create(text='Entry 2',list = correct_list)
        
        other_list = List.objects.create()
        Item.objects.create(text='other Entry 1',list = other_list)
        Item.objects.create(text='other Entry 2',list = other_list)
        response = self.client.get('/lists/%d/' % (correct_list.id,))
        self.assertContains(response,"Entry 1")
        self.assertContains(response,"Entry 2")
        self.assertNotContains(response,'other Entry 1')
        self.assertNotContains(response,'other Entry 2')
    def test_saving_a_post_request_to_an_existing_list(self):
        other_list = List.objects.create()
        correct_list = List.objects.create()
        self.client.post('/lists/%d/'%(correct_list.id),data = {'item_text':'A new list item for an existing list'})
        self.assertEqual(Item.objects.count(),1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text,'A new list item for an existing list')
        self.assertEqual(new_item.list,correct_list)
    def test_redirection_after_POST(self):
        other_list = List.objects.create()
        correct_list = List.objects.create()
        response=self.client.post('/lists/%d/'%(correct_list.id),data = {'item_text':'A new list item for an existing list'})
        self.assertRedirects(response,'/lists/%d/'%(correct_list.id))
    def test_validation_errors_are_displayed_on_the_homepage_itself(self):
        response = self.client.post('/lists/new',data={'item_text':''})
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'home.html')
        expected_error = "You cannot have an empty list item"
        self.assertContains(response,expected_error)
    def test_validation_of_saving_of_invalid_items(self):
        response = self.client.post('/lists/new',data={'item_text':''})
        #self.assertEqual(List.objects.count(),0)
        #self.assertEqual(Item.objects.count(),0)
        response = self.client.post('/lists/new',data={'item_text':'temp item'})
        #self.assertEqual(List.objects.count(),0)
        #self.assertEqual(Item.objects.count(),0)
