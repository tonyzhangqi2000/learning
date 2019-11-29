import unittest
from day0802.demo01_v1_register import MyComments
from day0802.test_parent import TestParent
import csv


class MyTestCase(TestParent):

    def test_comments(self):
        mc = MyComments(self.driver)
        mc.open("file:///C:/Users/ZhangQi/Downloads/seleniumday08/demo01.html")
        mc.type_name("张三")
        mc.type_password("123456")
        mc.click_male()
        mc.type_email("zhangqsan@126.com")
        mc.select_profession("法律相关")
        mc.click_food()
        mc.click_read()
        mc.type_comments("你好")
        mc.click_submit()

    def test_comments2(self):
        mc = MyComments(self.driver)
        mc.open("file:///C:/Users/ZhangQi/Downloads/seleniumday08/demo01.html")
        f = open("C:/Users/ZhangQi/Downloads/mydata1.csv")
        d = csv.reader(f)
        for row in d:
            mc.type_name(row[0])
            mc.type_password(row[1])
            mc.click_male()
            mc.type_email(row[2])
            mc.select_profession(row[3])
            mc.click_food()
            mc.click_read()
            mc.type_comments(row[4])
            mc.click_submit()


if __name__ == "__main__":
    unittest.main()
