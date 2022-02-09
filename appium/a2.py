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
    # 获取屏幕的高
    x = driver.get_window_size()['width']
    # 获取屏幕宽
    y = driver.get_window_size()['height']
    # 滑屏，大概从屏幕右边2分之一高度，往左侧滑动,滑动后显示的是 热点tab
    # driver.swipe(6 / 7 * x, 1 / 2 * y, 1 / 7 * x, 1 / 2 * y, 100)
    # time.sleep(4)
    # 向右滑动，显示推荐tab 内容，第五个参数，时间设置大一点，否则容易看不到滑动效果
    # driver.swipe(1 / 7 * x, 1 / 2 * y, 5 / 7 * x, 1 / 2 * y, 200)
    # time.sleep(4)
    # 向上滑
    # driver.swipe(1 / 2 * x, 1 / 2 * y, 1 / 2 * x, 1 / 7 * y, 200)
    # time.sleep(4)
    # 向下滑动
    driver.swipe(1 / 2 * x, 1 / 7 * y, 1 / 2 * x, 6 / 7 * y, 200)

# 向下滑动
swipeDown(driver)
time.sleep(2)

# 点开小程序
driver.find_element(By.ID,"com.tencent.mm:id/dty").click()
time.sleep(4)

print(driver.contexts)

# 注意，这里是不需要切换的，别踩坑了！！！！！！
# driver.switch_to.context('WEBVIEW_com.tencent.mm:toolsmp')
time.sleep(3)

#//*[@id="screenshotContainer"]/div/div/div/div/div/div[47]
#/html/body/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[47]
# //*[@id="sourceContainer"]/div/div[3]/div/div/div/div[31]/span[3]/span/span/b
# driver.find_element(By.XPATH,'//android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View[2]/android.view.View[2]/android.widget.Image[1]').click()

#试手气
driver.tap([(540,1058)],200)
time.sleep(10)

#礼包
#767 1352
def tap_gift():
    driver.tap([(767, 1352)], 200)
    time.sleep(2)
    print("点了礼包!")
    tap_receive()
#领取
#540 1320
def tap_receive():
    driver.tap([(540, 1320)], 200)
    time.sleep(2)
    print("点了领取!")
    tap_any_key()
    tap_me()

#点我点我
#540 1180
def tap_me():
    driver.tap([(540, 1180)], 200)
    time.sleep(2)
    print("点了小精灵1次!")
    tap_any_key()
    tap_back()


#任意键返回,精灵升级dialog会挡住点击小精灵
#565  320
def tap_any_key():
    driver.tap([(565, 320)], 200)
    time.sleep(1)
    print("点击了任意键!")

#返回
#64 148
def tap_back():
    driver.tap([(64, 148)], 200)
    time.sleep(1)
    print("点击了返回!")

tap_gift()

time.sleep(3)
print("结束...")
# input('**** Press to quit..')
# driver.quit()

# # tap触摸右下角那个菜单坐标 [873,1654], [1080,1861]
# driver.tap([(873, 1654), (1080, 1861)],  500)
#
# # 点发红包赚赏金
# driver.find_element_by_accessibility_id("发红包赚赏金").click()
