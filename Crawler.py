from   selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re
import pandas as pd
from selenium.webdriver.common.action_chains import ActionChains
import os
import operator

#launch url
#url = "http://kanview.ks.gov/PayRates/PayRates_Agency.aspx"
url = "https://www.codechef.com/ratings/all?order=asc&page=3&sortBy=global_rank"
# create a new Firefox session
driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get(url)
driver.implicitly_wait(10)
#Takes some time to load
soup=BeautifulSoup(driver.page_source, 'lxml')

k1=-1
links = soup.select('div.user-name > a')
x={}


for link in links:

    link2=link.get('href')
    driver.get("https://www.codechef.com"+str(link2))
    driver.implicitly_wait(3)
    soup=BeautifulSoup(driver.page_source, 'lxml')

    shit22=soup.find_all("div", class_="content")
    shitt= soup.select('div.user-name > a')
    anewshit=soup.find(string="Problems Solved")
    anewshit2=anewshit.find_parent("section")
    anweshit3=anewshit2.select(".content ")
    anweshit4=anewshit2.select_one(".content h5").contents[0]
    z=str(anweshit4)
    k1=int((re.findall(r'\d+', z))[0])
    x[link2]=k1


sorted_x = sorted(x.items(), key=operator.itemgetter(1))


print(sorted_x)




finalurl="https://www.codechef.com"+(str(sorted_x[-1][0]))

driver.get(finalurl)
print("Most questions are done by:"+finalurl)