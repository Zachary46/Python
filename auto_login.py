from selenium import webdriver

username = "username"
password = "password"
driver=webdriver.Chrome()
driver.get("https://passport.csdn.net/account/login")
driver.find_element_by_id("username").send_keys(username)
driver.find_element_by_id("password").send_keys(password)
driver.find_element_by_class_name("logging").click()
