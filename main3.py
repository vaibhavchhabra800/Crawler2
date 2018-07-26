from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re
import pandas as pd
import os
#url = "https://www.codechef.com/ratings/all?order=asc&page=3&sortBy=global_rank"
url = "http://kanview.ks.gov/PayRates/PayRates_Agency.aspx"

# create a new Firefox session
driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.get(url)



python_button = driver.find_element_by_id('MainContent_uxLevel1_Agencies_uxAgencyBtn_33') #FHSU
python_button.click() #click fhsu link
#print("DOES IT WORK")
#print(driver.page_source)
soup_level1=BeautifulSoup(driver.page_source, 'lxml')

datalist = [] #empty list
x = 0 #counter

for link in soup_level1.find_all('a', id=re.compile(r"^MainContent_uxLevel2_JobTitles_uxJobTitleBtn_")):
    ##code to execute in for loop goes here

    python_button = driver.find_element_by_id('MainContent_uxLevel2_JobTitles_uxJobTitleBtn_' + str(x))
    python_button.click() #click link

    #Selenium hands of the source of the specific job page to Beautiful Soup
    soup_level2=BeautifulSoup(driver.page_source, 'lxml')

    #Beautiful Soup grabs the HTML table on the page
    table = soup_level2.find_all('table')[0]

    #Giving the HTML table to pandas to put in a dataframe object
    df = pd.read_html(str(table),header=0)

    #Store the dataframe in a list
    datalist.append(df[0])

    #Ask Selenium to click the back button
    driver.execute_script("window.history.go(-1)")

    #increment the counter variable before starting the loop over
    x += 1
    if(x==5):
        break

print(datalist)
