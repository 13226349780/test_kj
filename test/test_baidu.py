import os
import time
from distutils.command.config import config

from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

from log.log import logger
from utils.config import Config, DATA_PATH
from utils.file_reader import ExcelReader


class TestBaiDu(unittest.TestCase):

    URL = Config().get('URL')
    excel = DATA_PATH + '/baidu.xlsx'
    #URL = 'http://baidu.com'
    locator_result = (By.XPATH, '//div[contains(@class, "result")]/h3/a')

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.URL)
    def tearDown(self):
        self.driver.quit()
    def test_search(self):
        datas = ExcelReader(self.excel).data
        for d in datas:
            with self.subTest(data = d):
                self.sub_setUp()
                self.driver.find_element_by_id('kw').send_keys(d['search'])
                self.driver.find_element_by_id('su').click()
                time.sleep(2)
                links = self.driver.find_elements(*self.locator_result)
                for link in links:
                    logger.info(link.text)
                self.sub_tearDown()

if __name__ == '__main__':
    unittest.main(verbosity=2)



