from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Firefox()
driver.implicitly_wait(20)
driver.get("http://192.168.154.129/ecshop")

try:
    loginButton = driver.find_element_by_xpath('//*[@id="ECS_MEMBERZONE"]/a[1]')
    loginButton.click()
    userInput = driver.find_element_by_name("username")
    userInput.send_keys("123")
    pwdInput = driver.find_element_by_name("password")
    pwdInput.send_keys("456")
    ljLoginButton = driver.find_element_by_name("submit")
    ljLoginButton.click()

    userInput = driver.find_element_by_name("username")
    userInput.send_keys("test")
    pwdInput = driver.find_element_by_name("password")
    pwdInput.send_keys("123456")
    ljLoginButton = driver.find_element_by_name("submit")
    ljLoginButton.click()
except NoSuchElementException as e:
    print("报错了：", e.msg)
finally:
    driver.quit()
