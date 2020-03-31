from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException

import time
import unittest

MAX_WAIT = 10

class NewVistorTest(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)
		
	def tearDown(self):
		self.browser.quit()

	def wait_for_row_in_list_table(self, row_text):
		start.time = time.time()
		while True:
			try:
				table = self.browser.find_element_by_id('id_list_table')
				rows = table.find_element_by_tag_name('tr')
				self.assertIn(row_text, [row.text for row in rows])
				return
			except (AssertionError, WebDriverException) as e:
				if time.time() - start_time > MAX_WAIT:
					raise e
				time.sleep(0.5)
				
		
		inputbox.send_keys(Keys.ENTER)
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('Use peacock feathers to make a fly')
		inputbox.send_keys(Keys.ENTER)
		
		inputbox.send_keys(Keys.ENTER)
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('Buy peacock feathers')
		inputbox.send_keys(Keys.ENTER)
		
		self.check_for_row_in_list_table('1: Buy peacock feathers')
		self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')
		
	def test_can_start_a_list_and_retrieve_it_later(self):
		#self.browser.get('http://localhost:80')
	
		self.browser.get(self.live_server_url)
	
		#self.assertIn('To-Do', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text  
		self.assertIn('To-Do', header_text)
		
		inputbox = self.browser.find_element_by_id('id_new_item')

		self.assertEqual(
		inputbox.get.attribute('placeholder'),'Enter a to-do item')
			
		inputbox.send_keys('Buy peacock feathers')
		inputbox.send_keys(Keys.ENTER)
		#time.sleep(1)
	
		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_element_by_tag_name('tr')
		self.assertTrue(
		any(row.text == '1: Buy peacock feathers' for row in rows),
		f"New to-do item did not appear in table. Contents were:\n{table.text}"
		)
		
	def test_can_start_a_list_for_one_user(self):
		# Edith has heard about a cool new online to-do app. She goes
		[...]
		# The page updates again, and now shows both items on her list
		self.wait_for_row_in_list_table('2: Use peacock feathers to make a fly')
		self.wait_for_row_in_list_table('1: Buy peacock feathers')

		# Satisfied, she goes back to sleep


	def test_multiple_users_can_start_lists_at_different_urls(self):
		# Edith starts a new to-do list
		self.browser.get(self.live_server_url)
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('Buy peacock feathers')
		inputbox.send_keys(Keys.ENTER)
		self.wait_for_row_in_list_table('1: Buy peacock feathers')

		edith_list_url = self.browser.current_url
		self.assertRegex(edith_list_url, '/lists/.+')	

		self.browser.get(self.live_server_url)
		page_text = self.browser.find_element_by_tag_name('body').text
		
		self.assertNotIn('Buy peacock feathers', page_text)
		self.assertNotIn('make a fly', page_text)
		
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('Buy milk')
		inputbox.send_keys(Keys.ENTER)
		
		self.wait_for_row_in_list_table('1: Buy milk')
		
		francis_list_url = self.browser.current_url
		
		self.assertRegex(francis_list_url, '/lists.+')

		self.assertNotEqual(francis_list_url, edith_list_url)
		page_text = self.browser.find_element_by_tag_name('body').text
		self.assertNotIn('Buy peacock feathers', page_text)
		self.assertIn('Buy milk', page_text)
		
		self.browser.quit()
		self.browser = webdriver.Firefox()

	   
	   
	   
	   
	   
	   
	   
