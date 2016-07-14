from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
class testclass(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
    def tearDown(self):
        self.browser.quit()
    
    def check_for_row_in_the_list_table(self,row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text,[row.text for row in rows])

    def test_first(self):
        self.browser.get(self.live_server_url)
        self.assertIn('To-Do',self.browser.title)
        
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do',header_text)

        input_box = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(input_box.get_attribute('placeholder'),'Enter a to-do item')
        
        input_box.send_keys("Learn Django")
        input_box.send_keys(Keys.ENTER)
        first_user_list_url =self.browser.current_url
        self.assertRegexpMatches(first_user_list_url,'/lists/.+')
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
        self.browser.get(self.live_server_url)
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
        print first_user_list_url
        print second_user_list_url
        self.assertEqual(first_user_list_url,second_user_list_url)
        self.fail("Finish the test !!")
