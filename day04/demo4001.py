from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Firefox



# 启动火狐浏览器
driver = Firefox()
# 打开01-id.html
driver.get("file:///C:/Users/ZhangQi/Downloads/seleniumday0401demo/01-id.html")
# 向姓名文本框中输入zhangsan
unInput = driver.find_element_by_id("username")
unInput.send_keys("zhangsan")
# 向密码框中输入123456
pwInput = driver.find_element(By.ID, "password")
pwInput.send_keys("123456")
# 提交
tjButton = driver.find_element_by_id("tijiao")
tjButton.click()
# 暂定4秒
sleep(4)
# 关闭浏览器
driver.quit()
