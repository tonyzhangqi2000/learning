from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import sleep


driver = webdriver.Firefox()
driver.get("http://192.168.154.129/ecshop")
# 定位列表框
cat = driver.find_element_by_id("category")
# 封装列表框类型的对象
cat_select = Select(cat) # type:Select
# 操作列表框：通过标号选择第三个选项（从0开始）
cat_select.select_by_index(2)
#cat_select.deselect_by_index(2) # 取消是能取消多选列表框
sleep(1)
# 操作列表框：通过值选择选项，value=12（充值卡）的
cat_select.select_by_value("12")
#cat_select.deselect_by_value("12")
sleep(1)
# 操作列表框：通过显示文本选择选项，充值卡
cat_select.select_by_visible_text("充值卡")
#cat_select.deselect_by_visible_text("充值卡")

cat_list = cat_select.options()
for item in cat_list:
    print(item.text)

sleep(1)
driver.quit()
