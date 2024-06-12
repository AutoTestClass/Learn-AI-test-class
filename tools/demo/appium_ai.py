from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from time import sleep


CAPS = {
    "deviceName": " MEIZU_E3",
    "automationName": "UiAutomator2",
    "platformName": "Android",
    "platformVersion": "7.1.1",
    "appPackage": " com.meizu.flyme.flymebbs",
    "appActivity": ".ui.LoadingActivity",
    "noReset": True,
    "unicodeKeyboard": True,
    "resetKeyboard": True,
    "customFindModules": {"ai": "test-ai-classifier"},
    "testaiConfidenceThreshold": 0.1,
    "shouldUseCompactResponses": False,
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', CAPS)
sleep(3)

# 用 AI 定位到搜索框
driver.find_element(AppiumBy.CUSTOM,"ai:search").click()
sleep(5)
driver.find_element(AppiumBy.ID, "com.meizu.flyme.flymebbs:id/kf").send_keys("flyme")

driver.find_element(AppiumBy.ID,"com.meizu.flyme.flymebbs:id/o7").click()
result = driver.find_element(AppiumBy.ID,"com.meizu.flyme.flymebbs:id/a2a")[0].text
print(result)

driver.quit()
