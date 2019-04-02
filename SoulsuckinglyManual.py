#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 18:27:27 2018

@author: caleb
"""
def update_to_one(last_range,tests):
    with open("pages/"+fname,"w+") as linkFile:
        for i in range(last_range,tests):
            temp = open("pages/OUTfile"+str(i)+".txt","r")
            linkNum=0
            for line in temp:
                if("jubao" in line):
                    continue
                elif("php" in line):
                    continue
                elif("trade"in line):
                    continue
                elif("shoucang" in line):
                    continue
                elif("login" in line):
                    continue
                elif("search" in line):
                    continue
                
                linkFile.write(line)
                linkFile.write("\n")
                linkNum+=1
            temp.close()
#
# new plan i guess.... 
# manually save  
#parse local html link index file, 
# add all to a list
# print list to pretty file
#
from bs4 import BeautifulSoup

url_list=[];
lastTest=1

test_num=3

fname="linkIndex.txt"

dir="/TaobaoWebScraper/pages/"
file=str(dir+"sj"+str(test_num)+".html")

raw_html = open(file,"r")
num=0
with open("pages/OUTfile"+str(test_num)+".txt","w+") as LinkFile:
    
   soup=BeautifulSoup(raw_html,"lxml")
   a=soup.find_all('a')
   for i in range(len(a)) :
       #print(a[i].get('href'))
       url = str(a[i].get('href'))
       if("item" in url):
           #print(url)
           LinkFile.write(url)
           LinkFile.write("\n")
           num+=1
       elif("world" in url):
           print("\n")
           #print(url)
           print("\n")
       url=""
raw_html.close()  
print(num)


update_to_one(lastTest,test_num)
"""


print("DONE WITH SELENIUM... TIME FOR SOUP...")
#give the page to soup
#with open("test.html") as fp :

soup1 = BeautifulSoup(driver.page_source,'lxml')

print(len(soup1))

datalist = []
x = 0

for link in soup_level1.find_all('a',id=re.compile("^MainContext_uxLevel2_JobTitles_uxJobTitleBtn_")):
    python_button = driver.find_element_by_id('MainContent_uxLevel2_JobTitles_uxJobTitleBtn_' + str(x))
    python_button.click()

"""
