import time
import sys
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

app_json = {
            "platformName": "Android",
            "deviceName": "R28M21YVXHF",
            "appPackage": "com.eg.android.AlipayGphone",
            "appActivity": "com.eg.android.AlipayGphone.AlipayLogin",
            "noReset": "true",
            "fullReset": "false",
            "automationName": "UiAutomator1"
            }

# get self's energy
def get_own(driver):
    TouchAction(driver).tap(x=440, y=600).perform()
    time.sleep(10)
    try:
        items = driver.find_elements_by_class_name("android.widget.Button")
        print(len(items))
        if len(items) > 5:
            for i in items:
                if '能量' in i.text:
                    i.click()
                    time.sleep(0.5)
    except:
        pass

# get friends' energy
def get_friends(driver):
    # swipe down to click more friends
    driver.swipe(720, 2800, 720, 800)
    time.sleep(0.5)
    driver.swipe(720, 2800, 720, 800)
    time.sleep(1)
    driver.find_element_by_xpath("//*[@text='View more friends']").click()
    time.sleep(5)

    # get friends' energy o(*￣▽￣*)ブ
    cnt = 1
    while cnt < 52:
        TouchAction(driver).press(x=235, y=935).release().perform()
        time.sleep(1)
        last_f = driver.find_element_by_id("com.alipay.mobile.nebula:id/h5_tv_title")
        if not last_f.text == '蚂蚁森林':
            # driver.tap([(710,440), (730,460)], 200)
            items = driver.find_elements_by_class_name("android.widget.Button")
            # print(len(items))
            if len(items) > 5:
                for i in items:
                    if '能量' in i.text:
                        i.click()
                        time.sleep(0.5)
            driver.tap([(21,178), (133,290)], 200)
            time.sleep(0.5)
            driver.swipe(157, 1126, 157, 874)
            time.sleep(0.5)
        else:
            TouchAction(driver).press(x=720, y=450).release().perform()
            time.sleep(0.5)
            sp_items = driver.find_elements_by_class_name("android.widget.Button")
            if len(sp_items) > 1:
                driver.tap([(21,178), (133,290)], 200)
                time.sleep(0.5)
            driver.swipe(157, 1126, 157, 874)
            time.sleep(0.5)
        cnt += 1

if __name__ == "__main__":
    server = "http://localhost:4723/wd/hub"
    driver = webdriver.Remote(server, app_json)
    time.sleep(15)
    # driver.tap([(112,851), (210,949)], 200)
    home_items = driver.find_elements_by_class_name("android.widget.TextView")
    ant_items = []
    for home_item in home_items:
        if home_item.text == "Ant Forest":
            ant_items.append(home_item)
    ant_items[-1].click()
    time.sleep(2)
    get_own(driver)
    get_friends(driver)
    driver.quit()