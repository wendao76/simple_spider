import platform
import os
import threading
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

appPath = os.path.dirname(__file__)
chromeOptions = Options()
chromeOptions.add_argument('--headless')
chromeOptions.add_argument('--disable-gpu')
chromeDriverPath = "";
if platform.system() == "Windows":
    chromeDriverPath = appPath + "/drivers/win32/chromedriver.exe"
elif platform.system() == "Linux":
    chromeDriverPath = appPath + "/drivers/linux64/chromedriver"


def start(url=""):
    opener = webdriver.Chrome(executable_path=chromeDriverPath, chrome_options=chromeOptions)
    opener.get('https://www.baidu.com')
    opener.find_element_by_id('kw').send_keys('测试')
    opener.find_element_by_id('su').click()
    opener.quit()


t = threading.Thread(target=start)
t.start()
