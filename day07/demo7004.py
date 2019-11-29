from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.get("http://192.168.154.129/ecshop/admin")

unInput = driver.find_element_by_name("username")
unInput.send_keys("admin")
pwdInput = driver.find_element_by_name("password")
pwdInput.send_keys("123asd!@#")
ccInput = driver.find_element_by_name("captcha")
ccInput.send_keys("0")
smtButton = driver.find_element_by_xpath('/html/body/form/table/tbody/tr/td[2]/table/tbody/tr[6]/td[2]/input')
smtButton.click()
sleep(1)
driver.switch_to.frame("header-frame")
outButton = driver.find_element_by_xpath('//*[@id="send_info"]/a[2]')
outButton.click()
sleep(1)
driver.quit()
