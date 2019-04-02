# TaoBao_WebScraper
A webscraper designed to obtain taobao user supplied reviews

Taobao, being an internet based company protects its servers using several anti-scraping methods. 
In order to avoid these anti-scraping methods and to conform to Taobao's robots.txt file the scraping was performed in several steps.

The first step includes finding the keywords for desired products and entering them into the search bar as a normal user would do.
The second step occurs when the user is presented with the results of the desired search. 

The results page is blocked from being analyzed by a robot, so these pages must be saved locally to the computer. 

--> user control + s to save the raw html to your computer
repeat steps one and two until we have a reasonable amount of pages on our computer. 

The third step uses Beautiful Soup to extract the desired links from the locally saved html pages.
This will result in a single text file containing links of desired pages to scrape. By doing this we conform to Taobao's robots.txt and still obtain the desired set of links that we will give to selenium to obtain the desired data.
--> soulSuckinglyManual.py is the script that performs this extraction
--> you will also need to clean the retrieved linkfile using updateLinks.py



The fourth step is where the data collection actually takes place. We give the obtained list of links to the selenium based web browser. It will find the comment section of the given page and select the secondary "   " comment section. Should second comments be present, Selenium will extract them to a local text file, using a special key to seperate each commment on the page. After iterating through comment pages until we recieve a timeout error or run out of comment pages, we save the text file locally and continue iterating through the given list of links until it has scraped all pages given.

-->getCommentsTMALL.py is the program that scrapes the individual pages for the comments
--> if you wish to get either good comments or bad comments, please use goodBadCommentTrainer.py
