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

class MangaDataManager:
    def __init__(self):
        self._crr_chapter = Chapter()

    # avoid already downloaded files & unaccessible chapter url
    def find_next_chapter(chapter):
        _crr_chapter = chapter 
        _crr_chapter.advance()
        # ToDo: access local disk and see if chapter is already there, advance chapter num accordingly
        # if !exist(chapter): chapter.advance()
        
        # ToDo: check if chapter exist on the web. That is, if !self.isAccessible() : chapter.advance()
    def current_chapter_url():
        return _crr_chapter.get_url();

class Chapter:
    def __init__(self, chapUrl):
        self.url = chapUrl
        self.chapter_num = 1 # ToDo: extract chapter number from the url 
    def advance():
        self.chapter_num += 1
    def get_url():
        # create string out of new chapter_num

chapter = Chapter(targetChapUrl)
mdMngr = MangaDataManager()
while mdMngr.find_next_chapter(chapter) != None:
    ImgDownloader.download_chapter(mdMngr)

