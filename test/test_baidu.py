import os
import time
from distutils.command.config import config

from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

from log.log import logger
from utils.config import Config


class TestBaiDu(unittest.TestCase):

    URL = Config().get('URL')
    #URL = 'http://baidu.com'
    locator_result = (By.XPATH, '//div[contains(@class, "result")]/h3/a')

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.URL)
    def tearDown(self):
        self.driver.quit()
    def test_search_0(self):
        self.driver.find_element_by_id('kw').send_keys('selenium 灰蓝')
        self.driver.find_element_by_id('su').click()
        time.sleep(2)
        links = self.driver.find_elements_by_xpath('//div[contains(@class, "result")]/h3/a')
        for link in links:
            logger.info(link.text)
    def test_search_1(self):
        self.driver.find_element_by_id('kw').send_keys('Python selenium')
        self.driver.find_element_by_id('su').click()
        time.sleep(2)
        #links = self.driver.find_elements(*self.locator_result)
        links = self.driver.find_elements_by_xpath('//div[contains(@class, "result")]/h3/a')
        for link in links:
            logger.info(link.text)


if __name__ == '__main__':
    unittest.main()



