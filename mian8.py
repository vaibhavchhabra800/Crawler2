from   selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re
import pandas as pd
from selenium.webdriver.common.action_chains import ActionChains
import os

#launch url
#url = "http://kanview.ks.gov/PayRates/PayRates_Agency.aspx"
url = "https://www.codechef.com/ratings/all?order=asc&page=3&sortBy=global_rank"
# create a new Firefox session
driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get(url)
memu
#Takes some time to load
print("h1")
soup=BeautifulSoup(driver.page_source, 'lxml')
print("h2")


links = soup.select('div.user-name > a')
for link in links:
    print(link.get('href'))
    link2=link.get('href')
    driver.get("https://www.codechef.com"+str(link2))
    driver.implicitly_wait(3)