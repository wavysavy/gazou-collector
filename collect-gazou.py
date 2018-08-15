# --
#  fetch image from a site containing images. Tested on windows only. It requires selenium and chrome driver.
#  populate the targetChapUrl below to test.
# --

import os
import time
import urllib
import urllib2
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options

targetChapUrl = '' #  to be populated to test

# get html via webdriver
options = webdriver.ChromeOptions()
options.add_argument("--disable-infobars")
options.add_argument("--incognito")

driver = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=options)  
driver.get(targetChapUrl)

html = driver.page_source

# ToDo: make this driver independent, use beautifulSoup instead
# get img urls and save it locally 
imgElms = driver.find_elements_by_tag_name('img')
driver.quit()

for ie in imgElms:
    imgUrl = ie.get_attribute('src') 
    print(imgUrl) 
    if len(imgUrl) < 255:
        urllib.urlretrieve(imgUrl, os.path.basename(imgUrl) )

