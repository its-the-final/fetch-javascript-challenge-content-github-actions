from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
#from webdriver_manager.utils import ChromeType

import time
options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
#driver_path = ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()
#driver = webdriver.Chrome(driver_path,options=options)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
#driver = webdriver.Chrome('/usr/src/ungoogled-chromium/chromedriver') 
driver.get("https://www.volksverpetzer.de/feed")
time.sleep(30) 
print(driver.page_source)
driver.close()