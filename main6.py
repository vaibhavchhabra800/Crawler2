from selenium import webdriver
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

#After opening the url above, Selenium clicks the specific agency link
# python_button = driver.find_element_by_id('ember488')
python_button = driver.find_element_by_xpath("//*[@id='ember"+str(489)+"']/td[2]/div[2]/a")


# #print(python_button)
# python_button.click() #click fhsu link

#Selenium hands the page source to Beautiful Soup
soup_level1=BeautifulSoup(driver.page_source, 'lxml')

datalist = [] #empty list
x = 488 #counter

# #Beautiful Soup finds all Job Title links on the agency page and the loop begins
# for link in soup_level1.find_all('a', id=re.compile("^MainContent_uxLevel2_JobTitles_uxJobTitleBtn_")):
#
#     #Selenium visits each Job Title page
#     python_button = driver.find_element_by_id('MainContent_uxLevel2_JobTitles_uxJobTitleBtn_' + str(x))
#     python_button.click() #click link
#



action=ActionChains(driver)




check1=20;
for link in soup_level1.find_all('a', id=re.compile(r"^ember")):

    driver.execute_script("window.scrollTo(0,"+ str(check1)+")")

    # code to execute in for loop goes here
    driver.implicitly_wait(20)
    print("check1")



    # python_button = driver.find_element_by_id('ember488')
    python_button = driver.find_element_by_xpath("//*[@id='ember"+str(x)+"']/td[2]/div[2]/a")
    #print(python_button)
    driver.implicitly_wait(20)

    action.move_to_element(python_button).click().perform()


    # python_button.click() #click fhsu link
    driver.execute_script("window.history.go(-1)")





    #Selenium hands of the source of the specific job page to Beautiful Soup
    # soup_level2=BeautifulSoup(driver.page_source, 'lxml')
    #
    # #Beautiful Soup grabs the HTML table on the page
    # table = soup_level2.find_all('table')[0]
    #
    # #Giving the HTML table to pandas to put in a dataframe object
    # df = pd.read_html(str(table),header=0)
    #
    # #Store the dataframe in a list
    # datalist.append(df[0])
    #
    # #Ask Selenium to click the back button
    # driver.execute_script("window.history.go(-1)")
    #
    # #increment the counter variable before starting the loop over
    x += 1
    check1+=1
    if(x>497):
        break


#     #end loop block
#
# #loop has completed
#
# #end the Selenium browser session
# driver.quit()
# licitly_wait