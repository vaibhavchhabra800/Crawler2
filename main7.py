
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re
import pandas as pd
import os
import time

url = "https://www.codechef.com/ratings/all?order=asc&page=3&sortBy=global_rank"
driver = webdriver.Firefox()
driver.get(url)
#Takes some time to load
time.sleep(5)
soup=BeautifulSoup(driver.page_source, 'lxml')

links = soup.select('div.user-name > a')
for link in links:
  print(link.get('href'))
