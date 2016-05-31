#!/usr/bin/python
# coding: utf-8
# -*- coding: utf-8 -*-


from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from django.contrib.staticfiles.testing import StaticLiveServerTestCase, LiveServerTestCase 

from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
import time
from django.core import mail
import re

class RegisterTest(LiveServerTestCase): 
    def setUp(self):
    	# self.driver = webdriver.Chrome()
    	self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(3)
        self.SERVER_URL=self.live_server_url
        self.driver.maximize_window()
        self.driver.get(self.SERVER_URL)
        mail.outbox=[]

    def tearDown(self):
        self.driver.quit()

    def test_register(self):
		register_in_link = self.driver.find_element_by_link_text("Register")  
		register_in_link.click()
		input_username =  self.driver.find_element_by_id("id_username")
		# print "input_username=", input_username
		# self.assertEquals(input_username,)
		self.assertTrue(input_username!=None)

        # ok_button.click()
		




