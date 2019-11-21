from time import sleep
from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://192.168.154.129/ecshop/")
#lybLink = driver.find_element_by_link_text("留言板")
#lyblink = driver.find_element_by_xpath("/html/body/div[3]/a[10]")
#lyblink = driver.find_element_by_xpath("//*[@id='mainNav']/a[10]")
#lyblink.click()
sleep(2)
#   打印第一个留言类型的文本
lyleixing = driver.find_element_by_name("msg_type")
lyleixings = driver.find_elements_by_name("msg_type")
print(lyleixing.get_attribute("value"), lyleixing.is_selected())
lyleixings[3].click()
sleep(2)
#   打印“欢迎光临本店”
hyguanglin = driver.find_element_by_id("ECS_MEMBERZONE")
print(hyguanglin.text)

driver.quit()
