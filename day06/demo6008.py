from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.get("http://192.168.154.129/ecshop")

print("首页")
print(driver.title)
print(driver.current_url)

# 登录按钮
loginButton = driver.find_element_by_xpath('//*[@id="ECS_MEMBERZONE"]/a[1]')
loginButton.click()
sleep(1)
print("登录页")
print(driver.title)
print(driver.current_url)

print("后退回首页")
driver.back()
print(driver.title)
print(driver.current_url)
sleep(1)

print("前进到登录页")
driver.forward()
print(driver.title)
print(driver.current_url)
sleep(1)

print("最小化")
driver.minimize_window()
sleep(1)

print("最大化")
driver.maximize_window()
sleep(1)

driver.quit()
