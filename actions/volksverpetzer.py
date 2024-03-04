from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
#from webdriver_manager.utils import ChromeType
from selenium_stealth import stealth

import time
chrome_options = Options()
options = [
   # "--headless",
   # "--disable-gpu",
    "--window-size=1920,1200",
    "--ignore-certificate-errors",
    "--disable-extensions",
    "--no-sandbox",
    "--disable-dev-shm-usage"
]
for option in options:
    chrome_options.add_argument(option)
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)

#driver_path = ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()
#driver = webdriver.Chrome(driver_path,options=options)
#driver = webdriver.Chrome('/usr/src/ungoogled-chromium/chromedriver') 
#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver = webdriver.Remote("127.0.0.1:4444/wd/hub", options=chrome_options)
#stealth(driver,
#        languages=["en-US", "en"],
#        vendor="Google Inc.",
#        platform="Win32",
#        webgl_vendor="Intel Inc.",
#        renderer="Intel Iris OpenGL Engine",
#        fix_hairline=True
#)
driver.get("https://www.volksverpetzer.de/feed")
time.sleep(10) 
#print(driver.page_source)
print(driver.execute_script('return document.getElementsByTagName("pre")[0].innerText'))

driver.close()