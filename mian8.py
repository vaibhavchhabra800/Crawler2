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
print("h1")
soup=BeautifulSoup(driver.page_source, 'lxml')
print("h2")

k1=-1
links = soup.select('div.user-name > a')
x={}
l1=0;

for link in links:

    link2=link.get('href')
    print(link2)
    #soup=BeautifulSoup(driver.page_source, 'lxml')
    driver.get("https://www.codechef.com"+str(link2))
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
    #print(anewshit)
    #print(anewshit2)
    #print("Time for shit3")
    #print(anweshit3)
    #print("Time for shit4")
    z=str(anweshit4)
    print(z)
    print(type((re.findall(r'\d+', z))[0]))
    print((re.findall(r'\d+', z)[0]))
    k1=int((re.findall(r'\d+', z))[0])
    print(type(str(anweshit4)))
    #print(anewshit[0].get_text())

    print("Ticket to Hoolywood")
    #soup.find("div", {"id": "articlebody"})


















    #soup=BeautifulSoup(driver.page_source, 'lxml')
    #print(soup)
    # shit22=soup.find_all("div", class_="content")
    # shitt= soup.select('div.user-name > a')
    # anewshit=soup.find(string="Fully Solved (296)")
    # anewshit2=anewshit.find_parents("h5")
    # print("Anewshit2=")
    # print(anewshit)
    # #print(anewshit[0].get_text())
    x[link2]=k1
    # print("Ticket to Hoolywood")
    # #soup.find("div", {"id": "articlebody"})
    #
    # blah=soup.find("div.content >h5 ")
    #print(shit22)
    #x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
    l1+=1




print("I DONT KNOW WHT IT IS doing it")
print(l1)
sorted_x = sorted(x.items(), key=operator.itemgetter(1))
print(type(sorted_x))

print(sorted_x)

print("Max questions are done by:")
print(x['/users/sumeet_varma'])
print(type(x))
print("BHAI CGHAl kya raha hai?")
print(str(sorted_x[-1][0]))
finalurl="https://www.codechef.com"+(str(sorted_x[-1][0]))
print(finalurl)
driver.get(finalurl)
print("Most questions are done by:"+finalurl)