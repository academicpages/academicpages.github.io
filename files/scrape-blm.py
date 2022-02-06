# let us encapsulate the whole process
import os,re,csv
import selenium
from selenium import webdriver
import time
import requests
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import ElementClickInterceptedException
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.by import By

# Let us define a couple of functions for ease of writing the loop
# first let us define a function to set up the driver
def driver_setup(url):
    # install the driver and initiate it
    driver = webdriver.Chrome(ChromeDriverManager().install())
    # url = "https://elephrame.com/textbook/BLM/chart"
    #driver.implicitly_wait(10)
    #driver.maximize_window()
    driver.get(url)
    time.sleep(20)
    return driver

# second let us define a function to scrape each page
def scrape_page(driver):
    '''Access driver page source, and scrape all the necessary info,
    return a list of vars named data'''
    # we get the first page, voila, initiate page_id=1
    page_id=1
    # Let us open a tsv file for saving our data
    with open('blm-data.tsv','w+') as f:
        tsv_writer = csv.writer(f, delimiter='\t')
        # write column names
        var_names=["page_id","protest_id", "protest_location","protest_start","protest_end","protest_subject","protest_participants", 
                "protest_time","protest_description", "protest_urls"]
        tsv_writer.writerow(var_names)
        # loop the website to get all pages
        while page_id<=336:
            try:
                driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
                page = driver.page_source
                soup = bs(page,"html.parser")
                items = soup.findAll("div",{"class":"item chart"})
                # iterating all items
                for item in items:
                    try:
                        protest_id=re.findall(r'id="([0-9].*?)"',str(item))[0]
                        print(protest_id)
                    except:
                        protest_id=""
                    try:
                        protest_location=' '.join(item.find("div",{"class":"item-protest-location"}).text.split())
                        print(protest_location)
                    except:
                        protest_location=""
                    try:
                        protest_start=' '.join(item.find("div",{"class":"protest-start"}).text.split())
                        print(protest_start)
                    except:
                        protest_start=""
                    try:
                        protest_end=' '.join(item.find("div",{"class":"protest-end"}).text.split())
                        print(protest_end)
                    except:
                        protest_end=""
                    try:
                        protest_subject=' '.join(item.find("li",{"class":"item-protest-subject"}).text.split())
                        print(protest_subject)
                    except:
                        protest_subject=""
                    try:
                        protest_participants=' '.join(item.find("li",{"class":"item-protest-participants"}).text.split())
                        print(protest_participants)
                    except:
                        protest_participants=""
                    try:
                        protest_time=' '.join(item.find("li",{"class":"item-protest-time"}).text.split())
                        print(protest_time)
                    except:
                        protest_time=""
                    try:
                        protest_description=' '.join(item.find("li",{"class":"item-protest-description"}).text.split())
                        print(protest_description)
                    except:
                        protest_description=""
                    try:
                        protest_urls='##'.join(item.find("li",{"class":"item-protest-url"}).text.split())
                        print(protest_urls,"\n")
                    except:
                        protest_urls=""
                    data=[page_id,protest_id, protest_location,protest_start,protest_end,protest_subject,protest_participants, 
                        protest_time,protest_description, protest_urls]
                    tsv_writer.writerow(data)
            except:
                print("SOMETHING IS WRONG...\n")
                break
            # click next page
            try:
                if page_id==336:
                  break
                else:
                  pass
                driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
                driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
                time.sleep(3)
                next_page = driver.find_element(By.XPATH, '//*[@id="blm-results"]/div[3]/ul/li[4]')
                next_page.click()
                time.sleep(3)
                # update page_id
                page = driver.page_source
                soup = bs(page,"html.parser")
                page_id = soup.find("input",{"class":"page-choice"})["value"]
                page_id = int(page_id)
                print(page_id)
            except:
                print("CLICKING NEXT PAGE FAILS...\n")
                break

def main():
    # set up the driver
    url = "https://elephrame.com/textbook/BLM/chart"
    driver = driver_setup(url)
    scrape_page(driver)
    
main()
