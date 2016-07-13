import unittest,time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class testclass(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
#		self.browser.implicitly_wait(3)
	def tearDown(self):
		self.browser.quit()
	def test_first(self):
		self.browser.get('http://localhost:8000')
		self.assertIn('To-Do',self.browser.title)
		
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do',header_text)

		input_box = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(input_box.get_attribute('placeholder'),'Enter a to-do item')
		
		input_box.send_keys("Learn Django")
		input_box.send_keys(Keys.ENTER)

		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertTrue(any(row.text == 'Learn Django' for row in rows),
                        "New to-do item didnt appear in table -- its text was:\n%s"%(table.text))
		
		self.fail("Finish the test !!")
if __name__ == '__main__':
	unittest.main()
