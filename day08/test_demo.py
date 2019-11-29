import unittest

from selenium import webdriver


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(20)

    def test_msg1(self):
        self.driver.get("http://192.168.154.129/ecshop")
        self.driver.find_element_by_link_text("留言板").click()
        self.assertEqual(self.driver.title, "留言板_ECSHOP演示站 - Powered by ECShop")

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
