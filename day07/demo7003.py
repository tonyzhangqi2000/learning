from time import sleep

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
# 实例化WebDriverWait对象
w1 = WebDriverWait(driver, 10, 0.5)
driver.get("http://192.168.154.129/ecshop/user.php")
userInput = driver.find_element_by_name("username")
userInput.send_keys("123")
pwdInput = driver.find_element_by_name("password")
pwdInput.send_keys("456")
ljLoginButton = driver.find_element_by_name("submit")
ljLoginButton.click()

# 定位器，元组
# un_locator = (By.NAME, "username")
ec1 = EC.presence_of_element_located((By.NAME, "username"))
userInput = w1.until(ec1)
userInput.send_keys("789")

sleep(1)
driver.quit()
