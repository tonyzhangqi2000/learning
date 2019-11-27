from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import sleep

driver = webdriver.Firefox()
driver.get("http://192.168.154.129/ecshop")

gaoji = driver.find_element_by_link_text("高级搜索")
gaoji.click()

bs = Select(driver.find_element_by_id("brand"))
bs.select_by_visible_text("联想")

gt = driver.find_element_by_name("goods_type")
gts = Select(gt)
gts.select_by_value("9")

gt = driver.find_element_by_name("goods_type")
gts = Select(gt)
ct = gts.first_selected_option.text
if ct == "精品手机":
    color = driver.find_element_by_name("attr[185]")
    cs = Select(color)
    cs.select_by_value("白色")

sleep(1)
driver.quit()
