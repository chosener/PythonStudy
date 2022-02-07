# coding:utf-8
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
import time

from selenium.webdriver.common.by import By

desired_caps = {
                'platformName': 'Android',
                'platformVersion': '10',
                'deviceName': '6637cffa',
                'appPackage': 'com.tencent.mm',
                'appActivity': '.ui.LauncherUI',
                'automationName': 'Appium',
                # 'unicodeKeyboard': True,
                # 'resetKeyboard': True,
                'noReset': True,
                'chromeOptions': {'androidProcess': 'com.tencent.mm:appbrand0'}
                }

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

time.sleep(10)

def swipeDown(driver, t=500, n=1):
    '''向下滑动屏幕'''
    l = driver.get_window_size()
    x1 = l['width'] * 0.5          # x坐标
    y1 = l['height'] * 0.15        # 起始y坐标
    y2 = l['height'] * 0.85         # 终点y坐标
    for i in range(n):
        driver.swipe(x1, y1, x1, y2,t)

# 向下滑动
swipeDown(driver)
time.sleep(2)

# 点开小程序
driver.find_element(By.ID,"com.tencent.mm:id/dty").click()
time.sleep(4)

print(driver.contexts)

# 注意，这里是不需要切换的，别踩坑了！！！！！！
# driver.switch_to.context('WEBVIEW_com.tencent.mm:tools')
time.sleep(3)

driver.find_element(AppiumBy.ACCESSIBILITY_ID,"签到任务").click()

# # tap触摸右下角那个菜单坐标 [873,1654], [1080,1861]
# driver.tap([(873, 1654), (1080, 1861)],  500)
#
# # 点发红包赚赏金
# driver.find_element_by_accessibility_id("发红包赚赏金").click()
