from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://192.168.154.130/ecshop/")
loginLink = driver.find_element_by_css_selector("#ECS_MEMBERZONE > a:nth-child(2)")
loginLink.click()
driver.quit()
