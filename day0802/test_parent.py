import unittest

from selenium import webdriver


class TestParent(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(20)

    def tearDown(self):
        self.driver.quit()
