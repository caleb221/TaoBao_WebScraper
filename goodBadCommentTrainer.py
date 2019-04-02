#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 18:51:55 2018

@author: caleb
"""

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.firefox.options import Options

#
# trainer data
# get good comments 
# get bad comments
#

def review_button(driver, xpath):
        try:
            rev_btn=driver.find_element_by_xpath(xpath)
            rev_btn.click()
        except Exception as e:
            print(e)
            return

def getComments(serverID,isTmall,file):
    #===========================================================================
    if isTmall:
        return False
    #taobao
    else:
        secondCom=driver.find_elements_by_class_name("tb-rev-item")
    #===========================================================================
    #black hole
    if len(secondCom) < 1:
        print("length less than 1?")
        return False
    
    print(len(secondCom))
    for i in range(len(secondCom)):
        #print(secondCom[i].text)
        f.write(secondCom[i].text)
        f.write("\n")
        f.write("==========")
        f.write("\n")
        #print("COMMENTS: ",len(commentData))
        #print(secondCom[i].text)
    return True;

def closeBtn():
    try:
        close = driver.find_element_by_id('sufei-dialog-close')
        close.click()
        return True
    except Exception as e:
            print(str(e))
            return False
# find the commments button, click it to activate javascript

 #===========================================================================           
def secondRadio(driver,isGood,firstTry):
    option=0
    try:
         #reviews-t-val1
         #good button or bad button?    
        if(isGood):
         #===========================================================================   
            b = driver.find_element_by_id("reviews-t-val1")
            option=1
            if(not firstTry):
                option=4
        #===========================================================================
        else:
         
            driver.implicitly_wait(300)
            #
            #cant find it...
            #
            #xpath2="//div[@id='reviews']/div/div/div/div/div/div/div/ul/li[3]/label/span/span"
            
            xpath1="//div[@id='reviews']/div/div/div/div/div/div/div[2]/ul/li[5]/label/span/span"
            b = driver.find_element_by_id("reviews-t-val0")
            
            try:
                cNum=driver.find_element_by_xpath(xpath1).text
            except Exception as e:
                print("==\nxpath1 failed\n==moving on\n")
                cNum="(0)"#driver.find_element_by_xpath(xpath2).text
                
                #<span class="tb-tbcr-num">
                    
                #   <span data-kg-rate-stats="neutral">(18)</span>
                   
                #   </span>
                
            #python strings are odd    
            cNum=list(cNum)
            cNum[0]=""
            cNum[len(cNum)-1]=""
            cantBe0="".join(cNum)
            
            option=2
            print("bad Comment Value")
            print(cantBe0)
            print("\n")
            
            if( int(cantBe0) == 0):
                print("no Bad Comments..")
                b = driver.find_element_by_id("reviews-t-val1")
                option=1
                
            if( not firstTry):
                b = driver.find_element_by_id("reviews-t-val1")
                option=4
        
        b.click()
        
    except Exception as e:
        print(str(e))
        return 0
    return option
        #taobao  2nd comments radio btn
   
#===========================================================================
#                           DIRECTORIES
#===========================================================================
goodDir="C:\\Users\\cseif\\Desktop\\pythonCrap\\TaobaoWebScraper\\goodComments\\comments_"
badDir="C:\\Users\\cseif\\Desktop\\pythonCrap\\TaobaoWebScraper\\badComments\\comments_"
gecko_driverDir="C:\\Users\\cseif\\Desktop\\pythonCrap\\geckoFolder\\geckodriver"
linkFileDir="C:\\Users\\cseif\\Desktop\\pythonCrap\\TaobaoWebScraper\\linkIndex_updated30s.txt"

comment_outFile=goodDir#saved in a seperate folder and indexed with a number
pageNum=8
#clean link list BEFORE running driver
links = [x for x in range(9000)]

#open the links
index=0
canContinue = True

#CHECK FOR COPIED LINKS -->
b4=0
b3=1
b2=2
b1=3
b5=4
b6=5
b7=6
current_num=len(links)
#for i in range(5,int(current_num)):
    #url[i]=0
    
#    if(str(links[b4]) in str(links[i])):
#        links[b4]=0
#        print("COPY!!")
#    elif(str(links[b3]) in str(links[i])):
#         links[b3]=0
#         print("COPY!!")
#    elif(str(links[b2]) in str(links[i])):
##        links[b2]=0
#        print("COPY!!")
#    elif(str(links[b2]) in str(links[i])):
#        links[b1]=0
#        print("COPY!!")
#    b4+=1
#    b3+=1
#    b1+=1



#ERASE TMALL LINKS -->
with open(linkFileDir,"r") as lFile:
    for line in lFile:
        if("detail.tmall" in line):
            continue
        
        links[index]=line
        #print(links[index])
        index+=1
    for i in range(6,int(current_num)):
    #url[i]=0
    
        if(str(links[b4]) in str(links[i])):
            links[b4]=0
            print("COPY!!")
        elif(str(links[b3]) in str(links[i])):
            links[b3]=0
            print("COPY!!")
        elif(str(links[b2]) in str(links[i])):
            links[b2]=0
            print("COPY!!")
        elif(str(links[b1]) in str(links[i])):
            links[b1]=0
            print("COPY!!")
        elif(str(links[b5]) in str(links[i])):
            links[b5]=0
            print("COPY!!!!!!")
        elif(str(links[b6]) in str(links[i])):
            links[b6]=0
            print("DAMN COPIES GTFO")
        elif(str(links[b7]) in str(links[i])):
            links[b7]=0
            print("FUCK COPIES!!!")
		
		
        b7+=1
        b6+=1
        b5+=1	
        b4+=1
        b3+=1
        b2+=1
        b1+=1
#
# shen me yi se
#
        
revBtnXP3="//ul[@id='J_TabBar']/li[3]/a"
revBtnXP2="//ul[@id='J_TabBar']/li[2]/a"

#TmallUser="rate-user-info"
#TmallDate="tm-rate-date"
#TaobaoUser="from-whom"
#TaobaoDate="tb-r-date"
#timeStamp=driver.find_elements_by_class_name("tm-rate-date")
#userData=driver.find_elements_by_class_name("rate-user-info")

#start firefox

#lets act as bing for a little bit..
profile = webdriver.FirefoxProfile()
profile.set_preference("general.useragent.override","Bingbot")

option = Options()
option.add_argument("--headless")

#ADD the user agent override, but how??
driver = webdriver.Firefox(executable_path=gecko_driverDir,options=option)#options=option, executable_path=gecko_driverDir)
pageCount=0
driver.implicitly_wait(50)#let the poor server rest    
#url_test="https://item.taobao.com/item.htm?spm=a230r.1.14.116.25604423ARfKvu&id=572670123255&ns=1&abbucket=19#detail"
for url in links:
    #make sure the URL is an actual URL
    if type(url) == type(int(0)):
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
        #css=div.J_KgRate_ReviewContent.tb-tbcr-content 
        #dateClass=TaobaoDate
        isTmall = False
    else:
        print("what link is this?? continuing")
        continue        
        
		
    if pageCount < pageNum:
        pageCount+=1
        print("already seen...moving on..")
        continue        
		
    print("using:  "+commentPath)
    #go to the next url
    
    if driver.current_url == url:
        print("copied url")
        continue

    driver.get(url)
    driver.implicitly_wait(50)#let the poor server rest    
    
    canContinue = closeBtn()

    print("Connected to: ",url)
    
    # login screen failed to close, refresh 
    # wait a bit, and then try again
    # if nothing, next page
    if canContinue == False:
        
        try:
           driver.refresh()
        except Exception as e:
           print("CANT REFRESH..continue")
           continue

        WebDriverWait(driver,20)
        canContinue = closeBtn()
        try:
            review_button(driver,revBtnXP2)
            canContinue=True
        except Exception as e:
            print(str(e))
            review_button(driver,revBtnXP3)
            canContinue = False
    
    if canContinue:
   #taobao  2nd comments radio btn
   # radioBtn=driver.find_element_by_id("reviews-t-val2")
   
        commentData=driver.find_elements_by_css_selector(commentPath)
        if len(commentData) < 1:
                print("no reviews, trying other button")
                review_button(driver,revBtnXP2)
                commentData=driver.find_elements_by_css_selector(commentPath)
                if len(commentData) < 1:
                    print("couldnt find the comments =(\n moving on...")
                    commentData=driver.find_elements_by_css_selector("div.J_KgRate_ReviewContent.tb-tbcr-content")
                    print("TRIED LONGER CSS.... DID IT WORK?????")
                    print(len(commentData))
                    print("skip anyway, because i dont know if it worked")
                    continue
                
        #======================\
        # SAVE THE COMMENTS!   \
        #======================\
        
        #recursive, false look at bad comments
        #first, if none it tries good comments
        
        canSecondComment = secondRadio(driver,False,True)
        
        if canSecondComment == 0:
            print("==\nsomething with second radio failed\n== ")
            isComments=False
            isPage=False
            review_button(driver,revBtnXP2)
        elif canSecondComment==1:
            isPage=True
            isComments = True
            comment_outFile=goodDir#"goodComments//comments_"
        elif canSecondComment == 2:
            comment_outFile=badDir #"badComments//comments_"
            isPage=True
            isComments = True
        
            # bad comments found!
            # get them all....
            # store in bad comments section
        
        #loop through all review pages
        
        # i need to figure out how NOT to write a file for
        # every page i visit.....
        
        for i in range(canSecondComment):
            print("pageNum",i)
            
            
            cPageCount=0
            
            if i == 1:
                
                testNext=secondRadio(driver,True,False)
                
                if testNext == 1:
                    print("GOODCOMENTS")
                    comment_outFile=goodDir#"goodComments//comments_"#
                elif testNext == 2:
                    print("BAD COMMENTS")
                    comment_outFile=badDir #"badComments//comments_"#
                    secondRadio(driver,False,False)
                    isPage=True
                elif testNext ==0:
                    print("TEST FAILED")
                    continue
                elif testNext ==4:
                    print("WHAT???")
                    isPage=True
                    comment_outFile=goodDir #"goodComments//comments_"#
            
            print("saving to: "+comment_outFile)
            
            if i>=2:
                continue
                                
            with open(comment_outFile+str(pageNum)+".txt","w",encoding="utf-8") as f:
                f.write(url)
                f.write("\n")
                while isPage:
                    try:
                        isComments = getComments(commentPath,isTmall,f)#,userClass,dateClass)
                        WebDriverWait(driver, 80).until(expected_conditions.invisibility_of_element_located((By.ID, 'ajax_loader')))
                    except Exception as e:
                        print("TIMEOUT")
                        driver.refresh() ## i need to quit this shit
                        isPage = False # dont do this...it needs to change
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
                    if (cPageCount ==5):
                        isPage = False
                        continue
                    if isPage:
                        cPageCount+=1
                        nav.click()
            
            #got all the comments....move on           
            print("\n\nNEXT PAGE --->\n\n")  
            
            #driver.delete_all_cookies()
            #lets keep count while were here
            pageNum+=1
    #failed to close sufei, move on
    else:
        continue

driver.close()