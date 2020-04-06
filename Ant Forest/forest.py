import time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

app_json = {
            "platformName": "Android",
            "deviceName": "", # input your deviceName, you can get it with adb
            "appPackage": "com.eg.android.AlipayGphone",
            "appActivity": "com.eg.android.AlipayGphone.AlipayLogin",
            "noReset": "true",
            "fullReset": "false",
            "automationName": "UiAutomator1" # delete this if fail to work
            }

server = "http://localhost:4723/wd/hub"
driver = webdriver.Remote(server, app_json)
time.sleep(2)
driver.find_element_by_xpath("//*[@text='Ant Forest']").click()
time.sleep(2)

# get self's energy
def get_own(driver):
    items = driver.find_elements_by_class_name("android.widget.Button")
    if len(items) > 5:
        for i in items:
            if '能量' in i.text:
                i.click()
                time.sleep(0.5)
    driver.tap([(21,178), (133,290)], 200)

# get friends' energy
def get_friends(driver):
    # swipe down to click more friends
    driver.swipe(720, 2800, 720, 800)
    driver.swipe(720, 2800, 720, 800)
    driver.find_element_by_xpath("//*[@text='View more friends']").click()
    time.sleep(1)

    # 'get' friends' energy o(*￣▽￣*)ブ
    while True:
        TouchAction(driver).press(x=235, y=935).release().perform()
        time.sleep(1)
        last_f = driver.find_element_by_id("com.alipay.mobile.nebula:id/h5_tv_title")
        if not last_f.text == '蚂蚁森林':
            items = driver.find_elements_by_class_name("android.widget.Button")
            if len(items) > 5:
                for i in items:
                    if '能量' in i.text:
                        i.click()
                        time.sleep(0.5)
            # get last one's and quit
            if last_f.text == "": #put the last friend's name such as: xxx's ant forest
                driver.tap([(21,178), (133,290)], 200)
                driver.tap([(21,178), (133,290)], 200)
                time.sleep(0.2)
                driver.swipe(720, 800, 720, 2800)
                driver.swipe(720, 800, 720, 2800)
                return
            driver.tap([(21,178), (133,290)], 200)
            time.sleep(0.5)
            driver.swipe(157, 1126, 157, 874)
            time.sleep(0.2)
        else:
            sp_items = driver.find_elements_by_class_name("android.widget.Button")
            if len(sp_items) > 1:
                driver.tap([(21,178), (133,290)], 200)
                time.sleep(0.5)
            driver.swipe(157, 1126, 157, 874)
            time.sleep(0.2)

if __name__ == "__main__":
    get_own(driver)
    get_friends(driver)
    driver.quit()