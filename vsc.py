from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

start_url="https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

browser=webdriver.Chrome()
browser.get(start_url)

time.sleep(10)

scraped_data=[]

def scrape():
    soup=BeautifulSoup(browser.page_source,"html.parser")

    brightStarTable=soup.find("table",attrs={"class","wikitable"})
    table_body=brightStarTable.find('tbody')

    table_rows=table_body.find_all('tr')

    for row in table_rows:
        table_cols=row.find_all('td')

        temp_list=[]

        for col_data in table_cols:
            data=col_data.text.strip()
            temp_list.append(data)
        scraped_data.append(temp_list)

scrape()

star_data=[]

for i in range(0,len(scraped_data)-1):
    Star_names=scraped_data[i][1]
    Distance=scraped_data[i][3]
    Mass=scraped_data[i][5]
    Radius=scraped_data[i][6]
    Lum=scraped_data[i][7]
    req_data=[Star_names,Distance,Mass,Radius,Lum]
    star_data.append(req_data)

headers=['Star_names','Distance','Mass','Radius','Luminosity']

star_df=pd.DataFrame(star_data,columns=headers)
star_df.to_csv("scraped data.csv",index=True,index_label="ID")





