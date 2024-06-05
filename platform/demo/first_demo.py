from selenium import webdriver
from selenium.webdriver.common.by import By
from applitools.selenium import Eyes, Target, Configuration
from conf import API_key

# 初始化 Selenium WebDriver
driver = webdriver.Chrome()

# 初始化 Applitools Eyes
eyes = Eyes()
eyes.api_key = API_key  # 把 'YOUR_API_KEY' 替换为你的 Applitools API Key

try:
    # 创建一个新的测试实例配置
    config = Configuration()
    config.app_name = 'Applitools Hello World Demo'
    config.test_name = 'Hello World Test with Links and Button'

    # 开始视觉测试
    with eyes.open(
            driver,app_name="Hello World App",
            test_name="Hello World Test",
            viewport_size={'width': 800, 'height': 600}):

        # 访问目标页面
        driver.get("https://applitools.com/helloworld")

        # 检查主页面
        print("step 1")
        eyes.check("Main Page", Target.window())  # 检查整个浏览器窗口的视觉

        # 点击第一个 diff 链接
        print("step 2")
        driver.find_element(By.CSS_SELECTOR, 'a[href="?diff1"]').click()
        eyes.check("Diff1 Page", Target.window())

        # 返回主页面
        print("step 3")
        driver.back()

        # 点击第二个 diff 链接
        print("step 4")
        driver.find_element(By.CSS_SELECTOR, 'a[href="?diff2"]').click()
        eyes.check("Diff2 Page", Target.window())

        # 返回主页面
        print("step 5")
        driver.back()

        # 点击按钮
        print("step 6")
        driver.find_element(By.TAG_NAME, 'button').click()

        # 检查按钮点击后的页面
        print("step 7")
        eyes.check("After Button Click", Target.window())

        # 结束视觉测试并关闭浏览器
        eyes.close()
finally:
    driver.quit()
    eyes.abort()
