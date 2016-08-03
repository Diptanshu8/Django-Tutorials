from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys
class testclass(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        for arg in sys.argv:
            if 'liveserver' in arg:
                cls.server_url = 'http://'+arg.split('=')[1]
                return
            super(testclass,cls).setUpClass()
            cls.server_url = cls.live_server_url
    @classmethod
    def tearDownClass(cls):
        if cls.server_url == cls.live_server_url:
            super(testclass,cls).tearDownClass()
    def setUp(self):
        self.browser = webdriver.Firefox()
    def tearDown(self):
        self.browser.quit()
    def check_for_row_in_the_list_table(self,row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text,[row.text for row in rows])
    
    def test_layout_and_stylling(self):
        #the user goes to the homepage
        #we have set the browser size static inorder to make sure that the text box appears in the middle
        self.browser.set_window_size(1024,768)
        self.browser.get(self.server_url)
        input_box = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(input_box.location['x']+input_box.size['width']/2,512,delta=5)
        input_box.send_keys("testing\n")
        input_box = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(input_box.location['x']+input_box.size['width']/2,512,delta=5)
"""
class temp_testclass(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
    def tearDown(self):
        self.browser.quit()

    def test_first(self):
        self.browser.get(self.server_url)
        self.assertIn('To-Do',self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do',header_text)

        input_box = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(input_box.get_attribute('placeholder'),'Enter a to-do item')
        
        input_box.send_keys("Learn Django")
        input_box.send_keys(Keys.ENTER)
        first_user_list_url =self.browser.current_url
        self.assertRegexpMatches(first_user_list_url,'/lists/(\d+)/')
        self.check_for_row_in_the_list_table('Learn Django')
        
        input_box = self.browser.find_element_by_id('id_new_item')
        input_box.send_keys("Learn Django in detail")
        input_box.send_keys(Keys.ENTER)

        #checking if a new unique URL is generated or not and on that unique URL are the user entries present
        self.check_for_row_in_the_list_table('Learn Django')
        self.check_for_row_in_the_list_table('Learn Django in detail')

        self.browser.quit()
        
        #now a new user walks in and wants to start a new list
        self.browser = webdriver.Firefox()
        
        #now this user visits our homepage and verfies that it doesn't have the contents of the previous user
        self.browser.get(self.server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Learn Django',page_text)
        self.assertNotIn('Learn Django in detail',page_text)

        #after confirming that data of previous user in not present, the new user starts filling in his own list
        input_box = self.browser.find_element_by_id('id_new_item')
        input_box.send_keys("Setup python rtmbot")
        input_box.send_keys(Keys.ENTER)
       
        #checking the new URL and webpage contents for the new user
        second_user_list_url =self.browser.current_url
        self.assertRegexpMatches(second_user_list_url,'/lists/.+')
        self.check_for_row_in_the_list_table('Setup python rtmbot')
        
        #checking if the URLs for first and second user are not same
        self.assertNotEqual(first_user_list_url,second_user_list_url)
   """ 
