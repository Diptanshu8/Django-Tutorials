from .base import FunctionalTest
from unittest import skip
from selenium import webdriver
class ItemValidationTest(FunctionalTest):    
    @skip("temporary skip")
    def test_verifying_that_the_userinput_isnot_blank(self):
        #THE USER GOES TO HOMEPAGE AND HITS THE SUBMIT BUTTON
        #BUT OUR WEBSITE SHOULD RETURN AND ERROR SAYING THAT EMPTY ENTRIES ARE NOT ALLOWED 
        #THEN THE USER ENTERS CORRECT ENTRY PRESSES ENTER AND THEREUPON AGAIN TRIES FOR EMPTY ENTRY WITH A FAILURE
        self.fail("Gabru")

