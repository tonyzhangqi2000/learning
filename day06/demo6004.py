from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.get("http://192.168.154.129/ecshop")

search = driver.find_element_by_name("imageField")
search.click()
sleep(1)
a1 = driver.switch_to.alert
a1.accept()
sleep(1)
driver.quit()
