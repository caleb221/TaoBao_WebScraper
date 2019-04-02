#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 19:19:17 2018

@author: caleb


how to start a firefox session 
 and scrape some javascript links
"""
#root@dbx1145:/home/david/zookteck# python test.py

#from selenium.webdriver.common.keys import Keys
#from bs4 import BeautifulSoup
#import re
#import pandas as pd
#from tabulate import tabulate
#import os
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.firefox.options import Options


"""
https://detail.tmall.com/item.htm?id=577345730738&ali_refid=a3_430583_1006:1109190383:N:xiaomi:9ae2b5a4e4128cc6e0e96005bd9e9617&ali_trackid=1_9ae2b5a4e4128cc6e0e96005bd9e9617&spm=a230r.1.14.3&sku_properties=10004:1617715035;5919063:6536025
notes
comments are in a javascript function
function(w,d) 
    window,document
<h4 class="hd">累计评价 <em class="J_ReviewsCount">
 i use selenium to navigate AND extract the data from 
    that $%^&*()(&* javascript
...is there a faster way?

make a straight up call to the server?

paths to comments
xpath=//ul[@id='J_TabBar']/li[3]/a

"""
def review_button(driver, xpath):
	try:
            rev_btn=driver.find_element_by_xpath(xpath)
            rev_btn.click()
	except Exception as e:
            print(e)
            return

def getComments(serverID,isTmall,file):#,userClass,dateClass):
    
    #tmall
    if isTmall:
        secondCom=driver.find_elements_by_class_name("tm-rate-append")   
    #taobao
    else:
        secondCom=driver.find_elements_by_css_selector("div.tb-rev-item.tb-rev-item-append")
    
    #black hole
    if len(secondCom) < 1:
        return
    
    #commentData=driver.find_elements_by_css_selector(serverID)
    print(len(secondCom))
    for i in range(len(secondCom)):
        #print(secondCom[i].text)
        f.write(secondCom[i].text)
        f.write("\n")
        f.write("==========")
        f.write("\n")
        
        #print("COMMENTS: ",len(commentData))

# login pages hiding the data
# --> close it before we can get to the comments
#surround with try/except...there might not always be a login page
#find the close button and click it
def closeBtn():
    #wait = WebDriverWait(driver,10)
    #wait.until(EC.element_to_be_clickable((By.ID, 'sufei-dialog-close')))
    try:
        close = driver.find_element_by_id('sufei-dialog-close')
        close.click()
        return True
    except Exception as e:
            print(str(e))
            return False
# find the commments button, click it to activate javascript
#rev_btn= driver.find_element(By.XPATH,'//ul[@id="J_TabBar"]/li[3]/a')
def secondRadio(isTmall, driver):
    if(isTmall):
        #tmall shit
        try:
            b = driver.find_element_by_class_name("rate-list-append")
        except Exception as e:
            print(str(e))
            return False
    else:
        try:
            b = driver.find_element_by_id("reviews-t-val2")
        except Exception as e:
            print(str(e))
            return False
    b.click()
    return True
        #taobao  2nd comments radio btn
            
            
#website to search
#TEST PAGE

#url="https://detail.tmall.com/item.htm?spm=a230r.1.14.1.398f5e4cyRDCha&id=525248995106&cm_id=140105335569ed55e27b&abbucket=16&sku_properties=5919063:6536025"
#this review list was on index 2 instead of 3..?
#exception handled, try the other button
# i wonder if i should add more indexes? 

#url="https://detail.tmall.com/item.htm?spm=a230r.1.14.117.7e421aadDk65KN&id=550193007128&ns=1&abbucket=16"
#url="https://detail.tmall.com/item.htm?spm=a230r.1.14.194.7e421aadDk65KN&id=550424903809&ns=1&abbucket=16"
#https://click.simba.taobao.com/cc_im?p=oppo&s=111870457&k=537&e=xsQE9TzjDr7VafSFhj6mWjVthLyPQLtEGk2jHjPA0V9tr3o9G8afeMs1joAumx4ezwgZ0OoRsqMFf28y4rVkGzCI8hnmhNBXrd8wB4RKVPHGQRVdR5jikxZdaKlL66REqrxrqsjOw1iN0C2P98gxd1Xz6RRfgjwDcPvicTyK%2FBLdbVh2CVRdP4eQTFZQOf1Y0OgskLp2XbPQqXLmm6Tgps2ZMRUpnkjnn9IH5ovX3L3Bl8AYQ%2FC3oBeTwVggqPm6A3qkPoyzUr7Tq1Ze8mXl0QxX%2FfpbCt6Fpq7t0fNXYMRUsUFLDo4LYuhiS8Ujt2I2bzCz5W5OEJs%2FlAw2LYHcPEO8v8xTbHiwgUUD7pjWfWR62vZPlVpqzuaAPHz2yI6aHzhukmpwjeqTFQIpZ4lf2RzQ3vB4KQ65jVN2%2FamkZZEVRzoYeQSFt833jNG1LZvpqXd2Z9BE5QC%2B3DtkUCHXZhYbZuXeKXQ%2BB7Vycxh0Hk%2FC0X5u%2F%2BtdYorJTUJFa6AA2N2Ci46b3nzyHxB5p8EdKg%3D%3D
#url="https://item.taobao.com/item.htm?id=576105946749&ns=1&abbucket=14#detail"
#url="https://detail.tmall.com/item.htm?spm=a220m.1000858.1000725.9.4f6e766aDCG5Y4&id=566603286049&skuId=3960946098953&standard=1&user_id=2838892713&cat_id=2&is_b=1&rn=5d12ee06a3022f33614ee7980e4feb1b"#"https://detail.tmall.com/item.htm?spm=a220m.1000858.1000725.9.4f6e766aDCG5Y4&id=566603286049&skuId=3960946098953&standard=1&user_id=2838892713&cat_id=2&is_b=1&rn=5d12ee06a3022f33614ee7980e4feb1b"
#url="https://item.taobao.com/item.htm?id=561846505061&ns=1&abbucket=0#detail"
links = [x for x in range(3000)]

#open the links
index=0
canContinue = True  
with open("C:\\Users\\cseif\\Desktop\\pythonCrap\\TaobaoWebScraper\\ChipsIndex.txt","r") as lFile:
    for line in lFile:

        links[index]=line
        index+=1
        
revBtnXP3="//ul[@id='J_TabBar']/li[3]/a"
revBtnXP2="//ul[@id='J_TabBar']/li[2]/a"
#TmallUser="rate-user-info"
#TmallDate="tm-rate-date"
#TaobaoUser="from-whom"
#TaobaoDate="tb-r-date"
#timeStamp=driver.find_elements_by_class_name("tm-rate-date")
#userData=driver.find_elements_by_class_name("rate-user-info")

#========================================================
# GET ONLY 2ND COMMENTS
# --> NOT TMALL ( TAOBAO SERVER)
outfile = "C:\\Users\\cseif\\Desktop\\pythonCrap\\TaobaoWebScraper\\comments\\2nd_Chipscomments_"
#start firefox
skipFile= "https://item.taobao.com/item.htm?id=576653767544&ns=1&abbucket=14"
option = Options()
option.add_argument("--headless")
gecko_path="C:\\Users\\cseif\\Desktop\\pythonCrap\\geckoFolder\\geckodriver"
driver = webdriver.Firefox(executable_path=gecko_path,options=option)

driver.implicitly_wait(50)#let the poor server rest    
pageNum=96

skipper=96
for url in links:
    #make sure the URL is an actual URL
    if type(url) == type(int(0)):
        continue
		
    if skipper < pageNum:
        print("ALREADY EVALD PAGE...NEXT....")
        skipper +=1
        continue
    
#===read in the list of URLS... i should make this a top
#level functionality
#grabbing comments should probably take in a URL 
    if "tmall" in url: 
        print ("tmall link!")
        commentPath="div.tm-rate-fulltxt"
        #userClass=TmallUser
        #dateClass=TmallDate
        isTmall=True
    elif "click.simba" in url:
        print ("simba link, redirect to tmall..")
        commentPath="div.tm-rate-fulltxt"
        #userClass=TmallUser
        #dateClass=TmallDate
        isTmall=True
    elif "item.taobao" in url:
        print("not tmall, trying tb server")
        commentPath =".tb-tbcr-content"
        #userClass=TaobaoUser
        #dateClass=TaobaoDate
        isTmall = False
    else:
        print("what link is this?? continuing")
        continue        
        
    print("using:  "+commentPath)
    #go to the next url
    if skipFile in url:
        continue
    if driver.current_url == url:
        print("copied url")
        continue
    try:
        driver.get(url)
    except Exception as e:
        print("bad URL???")
        continue
	
    driver.implicitly_wait(50)#let the poor server rest    

    print("Connected to: ",url)

    canContinue = closeBtn()
    
    #login screen failed to close, refresh 
    # wait a bit, and then try again
    #if nothing, next page
    if canContinue == False:
        WebDriverWait(driver,20)
        driver.refresh()       
        canContinue = closeBtn()
    
    
    if canContinue:
       
        try:
            review_button(driver,revBtnXP3)
        except Exception as e:
            print(str(e))
            review_button(driver,revBtnXP2)
        
    #taobao  2nd comments radio btn
   # radioBtn=driver.find_element_by_id("reviews-t-val2")
    
   
        commentData=driver.find_elements_by_css_selector(commentPath)
        if len(commentData) < 1:
                print("no reviews, trying other button")
                review_button(driver,revBtnXP2)
                commentData=driver.find_elements_by_css_selector(commentPath)
                if len(commentData) < 1:
                    print("couldnt find the comments =(\n moving on...")
                    continue
        #======================\
        # SAVE THE COMMENTS!   \
        #======================\
        canSecondComment = secondRadio(isTmall,driver)
        
        if canSecondComment == False:
            print("didnt find the comment button, try other page")
            review_button(driver,revBtnXP2)
            
        #loop through all review pages
        isPage=True
        # i need to figure out how NOT to write a file for
        # every page i visit.....
        with open(outfile+str(pageNum)+".txt","w",encoding="utf-8") as f:
            f.write(url)
            f.write("\n")
            pageCount=0
            while isPage:
                try:
                    getComments(commentPath,isTmall,f)#,userClass,dateClass)
                    WebDriverWait(driver, 30).until(expected_conditions.invisibility_of_element_located((By.ID, 'ajax_loader')))
                except Exception as e:
                    print("TIMEOUT")
                    driver.refresh() ## i need to quit this
                    isPage = False ## dont do this...it needs to change
                    continue
                
                if isTmall:
                    try:
                        nav = nav=driver.find_element_by_partial_link_text("下一页")
                    except Exception as e:
                        print(str(e))
                        isPage = False
                        continue
                else:
                    try:
                        nav = driver.find_element_by_class_name("pg-next")
                    except Exception as ee:
                        print(str(ee))
                        isPage = False
                        continue
                if isPage:
                    nav.click()
                if(pageCount == 14):
                    isPage = False
                    continue
                pageCount+=1
            #got all the comments....move on
            
            print("\n\nNEXT PAGE --->\n\n")  
            driver.delete_all_cookies()
            #lets keep count while were here
            pageNum+=1
            
    #failed to close sufei, move on
    else:
        continue

driver.close()
