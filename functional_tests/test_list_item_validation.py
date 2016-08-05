from .base import FunctionalTest
from unittest import skip
from selenium import webdriver
class ItemValidationTest(FunctionalTest):    
    def test_verifying_that_the_userinput_isnot_blank(self):
        #THE USER GOES TO HOMEPAGE AND HITS THE SUBMIT BUTTON
        #BUT OUR WEBSITE SHOULD RETURN AND ERROR SAYING THAT EMPTY ENTRIES ARE NOT ALLOWED 
        #THEN THE USER ENTERS CORRECT ENTRY PRESSES ENTER AND THEREUPON AGAIN TRIES FOR EMPTY ENTRY WITH A FAILURE
        
        #the user goes to our website and enters a blank entry
        self.browser.get(self.server_url)
        self.browser.find_element_by_id('id_new_item').send_keys('\n')

        #the homepage refreshes with an error message
        error = self.browser.find_element_by_css_selector('.has_error')
        self.assertEqual(error.text,'You cannot have an empty list item')

        #now the user tries again with a proper list item
        self.browser.find_element_by_id('id_new_item').send_keys('Buy Milk\n')
        self.check_for_row_in_the_list_table("Buy Milk")

        #now the user tries to send a second blank entry in the item submission box
        self.browser.find_element_by_id('id_new_item').send_keys('\n')
        
        #the user again recieves a similar warning about the empty entry item
        self.check_for_row_in_the_list_table("Buy Milk")
        error = self.browser.find_element_by_css_selector('.has_error')
        self.assertEqual(error.text,'You cannot have an empty list item')

        #looking at the error the user deciedes to modify the item entry to a valid entry
        self.browser.find_element_by_id('id_new_item').send_keys('Buy Tea\n')
        self.check_for_row_in_the_list_table("Buy Milk")
        self.check_for_row_in_the_list_table("Buy Tea")

        self.fail("Gabru")

