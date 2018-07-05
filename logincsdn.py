#!/usr/bin/python3
from selenium import webdriver
import time
import webbrowser

def start():
    driver = webdriver.Chrome('/Users/zachary/zachary/chromedriver.exe')
    driver.get("https://passport.csdn.net/account/login")
    print("打开csdn登陆界面")
    driver.find_element_by_class_name("login-code__open").click()
    print("切换到账号登陆")
    time.sleep(2) #防止元素还没加载出来就操作报错
    driver.find_element_by_id('username').clear()
    driver.find_element_by_id('username').send_keys('Zachary_46')  # 这里填写你的QQ号
    driver.find_element_by_id('password').clear()
    driver.find_element_by_id('password').send_keys('csdn.19930105')
    driver.find_element_by_class_name('logging').click()
    time.sleep(2)
    driver.get("https://www.csdn.net/")
    #webbrowser.open_new("https://www.csdn.net/")
    time.sleep(1)
    html = driver.page_source
    print(html)

start()

