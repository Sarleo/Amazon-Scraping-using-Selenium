# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 14:52:49 2018

@author: saranshmohanty
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time
import os
#######################put your working directory#############################
os.chdir('C:/Users/saranshmohanty/Desktop/')

Trial=[]
##################################collecting top products######################

keyword=input("enter keyword\n")
##########################first execute till here and check the items in Product#######################################33





keyword=keyword.lower()
driver=webdriver.Firefox()
#driver.get("https://www.google.com")
Products=[]
driver.get("https://www.amazon.com")
#keyword='adidas'
elem5 = driver.maximize_window
elem2= driver.find_element_by_css_selector("#twotabsearchtextbox")
elem2.clear()
elem2.send_keys(keyword)
#time.sleep(5)

elemx=driver.find_element_by_css_selector('.nav-sprite .nav-input')
elemx.click()

#elem22 = driver.find_elements_by_css_selector('#result_20 .s-access-title')
lenprod=0


#########################################it will take the top 100 products########################
while len(Products) <=20:
    elem22 = driver.find_elements_by_css_selector('.s-access-title')
    for i in elem22:
        if(keyword in i.text):
            Products.append(i.text)
        else:
            Products.append(keyword+' '+i.text)
        if(len(Products)>20):
            break
    elem33=driver.find_element_by_css_selector('#pagnNextString')
    elem33.click()
    time.sleep(5)            

#########################################top 100 products taken########################################

driver.get("https://www.amazon.com")
elem5 = driver.maximize_window

result=[]
ratings=[]
for prod in Products:
    #driver.get("https://www.amazon.com")    
    #time.sleep(5)
    elem2= driver.find_element_by_css_selector("#twotabsearchtextbox")
    elem2.clear()
    elem2.send_keys(prod)
    #time.sleep(5)
    
    elemx=driver.find_element_by_css_selector('.nav-sprite .nav-input')
    elemx.click()
    time.sleep(5)
    ######################################click first element################################
    driver.execute_script("window.scrollTo(0, 220)") 
    elem3=driver.find_element_by_css_selector("#result_0 .s-access-title")
    #time.sleep(10)
    elem3.click()
    #time.sleep(5)
    ######################################click all reviews###################
    try:
        elem4=driver.find_element_by_css_selector("#reviews-medley-footer .a-text-bold")
        elem4.click()
        time.sleep(5)
    except:
        continue
    ############################most recent##########################
    elem5=driver.find_element_by_css_selector("#a-autoid-4-announce")
    elem5.click()
    time.sleep(5)
    elem6=driver.find_element_by_css_selector("#sort-order-dropdown_1")
    elem6.click()
    elem7 = driver.find_element_by_css_selector(".arp-rating-out-of-text")
    rating=elem7.text                                           
    ratings.append((prod,rating))
    count=0
    Trial=[]
    flag=False
    Name=[]
    Date=[]
    Review=[]
    One_liner=[]
    
    while(count<100 and flag==False):
        #driver.refresh
        time.sleep(5)
        ##################name of person#######################
        name_elem=driver.find_elements_by_css_selector(".a-profile-name")
        for i in name_elem:
            trial=i.text
            Name.append(trial)
        
        #print("name taken")
        time.sleep(2)
        ###########################review date############################
        date_elem=driver.find_elements_by_css_selector(".review-date")
        for j in date_elem:
            trial=j.text
            Date.append(trial)
        #print("date taken")
        #################################content of review################
        review_elem=driver.find_elements_by_css_selector(".review-text")
        for k in review_elem:
            trial=k.text
            Review.append(trial)
        #print("review taken")
        count=len(Name)
        ########################one liner################################
        oneLine_elem=driver.find_elements_by_css_selector(".a-color-base")
        for l in oneLine_elem:
            trial=l.text
            One_liner.append(trial)
        #print("one liner taken")
        try:
            nextbut=driver.find_element_by_partial_link_text("Next")
            nextbut.click()
            #print("next clicked")
            time.sleep(10)
            
        except:
            flag=True
            #print("no next")
            break
    
    print(len(ratings))
    
    
    for m in range(0,len(Review)):
        result.append((Date[m],Name[m],One_liner[m],Review[m],prod))
a_amazon=keyword +" amazon review"
#b=a+".csv"
b_amazon=a_amazon+".csv"
Final=[]
Final=pd.DataFrame(list(result))
Final.columns=['Date','Name','One liner','Review','Product']
Final.to_csv(b_amazon,encoding='utf-8',index=False)
