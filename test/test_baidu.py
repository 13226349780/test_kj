import os
import time
from distutils.command.config import config

from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

from utils.config import Config


class TestBaiDu(unittest.TestCase):

    #URL = Config().get('URL')
    URL = 'http://baidu.com'


    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.URL)
    def tearDown(self):
        self.driver.quit()
    def test_search_0(self):
        self.driver.find_element_by_id('kw').send_keys('selenium 灰蓝')
        self.driver.find_element_by_id('su').click()
        time.sleep(2)
    def test_search_1(self):
        self.driver.find_element_by_id('kw').send_keys('Python selenium')
        self.driver.find_element_by_id('su').click()
        time.sleep(2)

if __name__ == '__main__':
    unittest.main()



