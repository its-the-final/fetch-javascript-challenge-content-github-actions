from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
#from webdriver_manager.utils import ChromeType
from selenium_stealth import stealth

import time
chrome_options = Options()
options = [
    "--headless",
    "--disable-gpu",
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
stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True
)
#driver_path = ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()
#driver = webdriver.Chrome(driver_path,options=options)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
#driver = webdriver.Chrome('/usr/src/ungoogled-chromium/chromedriver') 
driver.get("https://www.volksverpetzer.de/feed")
time.sleep(23) 
print(driver.page_source)
driver.close()