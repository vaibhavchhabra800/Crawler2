from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import bs4,requests
import re
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
import os
from selenium.webdriver.support.ui import WebDriverWait
#import java.util.concurrent.TimeUnit


url = "https://www.google.com"
#url = "https://www.codechef.com/ratings/all?order=asc&page=3&sortBy=global_rank"
#url = "http://kanview.ks.gov/PayRates/PayRates_Agency.aspx"

# create a new Firefox session
driver = webdriver.Firefox()
#driver.implicitly_wait(30)
res=requests.get(url)
soup_level1=bs4.BeautifulSoup(res.text, 'lxml')

#soup_level1=2
#python_button = driver.find_element_by_id('MainContent_uxLevel1_Agencies_uxAgencyBtn_33') #FHSU
#python_button.click() #click fhsu link
#print("DOES IT WORK")
#print(driver.page_source)
#soup_level1=BeautifulSoup(driver.page_source, 'lxml')

datalist = [] #empty list
x = 488 #counter
#driver.manage().window().maximize();





#driver.get("http://somedomain/url_that_delays_loading")

#elem11=driver.find_element_by_id('ember488')
elem11=soup_level1('#ember488')


# guru99seleniumlink= wait.until(ExpectedConditions.visibilityOfElementLocated(By.xpath( "/html/body/div[1]/section/div[2]/div/div[1]/div/div[1]/div/div/div/div[2]/div[2]/div/div/div/div/div[1]/div/div/a/i")));
# guru99seleniumlink.click();



# try:
#     element=100
#     element = WebDriverWait(driver, 10).until(
#         #expected_conditions.visibility_of_element_located((By.XPATH,"//*[@id='ember"+str(493)+"']/td[2]/div[2]/a"))
#
#         expected_conditions.visibility_of_element_located((By.ID,"ember488"))
#     )
# except:
#     print("damnit")















#driver.manage().timeouts().implicitlyWait(2, TimeUnit.SECONDS);
#driver.implicitly_wait(3)
print(driver.page_source)
for link in soup_level1.find_all('a', id=re.compile(r"^ember")):
    ##code to execute in for loop goes here
    driver.implicitly_wait(30)
    print("check1")
    driver.implicitly_wait(30)
    elemnt2222=driver.find_element_by_xpath("//*[@id='ember"+str(493)+"']/td[2]/div[2]/a")

    #python_button = driver.find_element_by_id('ember' + str(x))
    python_button = elemnt2222
    python_button.click() #click link

    #Selenium hands omanagef the source of the specific job page to Beautiful Soup
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

