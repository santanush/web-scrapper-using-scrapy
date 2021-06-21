# web-scrapper-using-scrapy
A Sample Web Scrapper using python scrappy that can scrap information's from multiple pages 

# Overview
This project uses python spider for crawling all mobile phones available in India alosng with price from https://pricebaba.com/
The informations are maintianed within the URL https://pricebaba.com/mobile/pricelist/all-mobiles-sold-in-india and contains pagination with multiple pages.
The spider class uses xpath to evaluate comon information from each page until the pagination with mobile informations are available.

# Crawl A Web Page with Scrapy and Python 3

### Step1 install scrapy
    pip install scrapy
### Step2 Creating a new Scrapy project
    scrapy startproject webspider
### Step3 Implement the parser class 
    For this example PriceBabaMobileListParser

### Step4 Execute the spider with the below command and save the output in CSV in your computer
    scrapy crawl mobileParser -o "file:///C:/Workspace/GIT_Workspace/web-scrapper-using-scrapy/csv/mobilesInIndia.csv" -t csv

    
    


