from   selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re
import pandas as pd
from selenium.webdriver.common.action_chains import ActionChains
import os
import operator

# create a new Firefox session
driver = webdriver.Firefox()
driver.implicitly_wait(3)


#soup=BeautifulSoup(driver.page_source, 'lxml')
driver.get("https://www.codechef.com/users/sumeet_varma")
driver.implicitly_wait(3)






soup=BeautifulSoup(driver.page_source, 'lxml')
#print(soup)
shit22=soup.find_all("div", class_="content")
shitt= soup.select('div.user-name > a')
anewshit=soup.find(string="Problems Solved")
anewshit2=anewshit.find_parent("section")
anweshit3=anewshit2.select(".content ")
anweshit4=anewshit2.select_one(".content h5").contents[0]



print("Anewshit2=")
print(anewshit)
print(anewshit2)
print("Time for shit3")
print(anweshit3)
print("Time for shit4")
z=str(anweshit4)
print(z)
print(type(int((re.findall(r'\d+', z))[0])))
print((re.findall(r'\d+', z)[0]))

print(type(str(anweshit4)))
#print(anewshit[0].get_text())

print("Ticket to Hoolywood")
#soup.find("div", {"id": "articlebody"})

blah=soup.find("div.content >h5 ")
#print(shit22)
#x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

driver.implicitly_wait(3)
