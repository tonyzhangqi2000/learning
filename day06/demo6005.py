from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.get("http://192.168.154.129/ecshop/goods.php?id=24")

certButton = driver.find_element_by_xpath('//*[@id="ECS_FORMBUY"]/ul/li[9]/a[1]')
certButton.click()
sleep(1)
deleteButton = driver.find_element_by_xpath('//*[@id="formCart"]/table[1]/tbody/tr[2]/td[7]/a')
deleteButton.click()
sleep(1)
a1 = driver.switch_to.alert
print(a1.text)
# 取消
a1.dismiss()
# 确定
#a1.accept()
sleep(1)
driver.quit()
