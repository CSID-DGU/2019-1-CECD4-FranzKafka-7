from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys
import datetime as dt

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
browser = webdriver.Chrome('chromedriver', chrome_options=options)

startdate=dt.date(year=2015,month=2,day=6)
untildate=dt.date(year=2015,month=2,day=7)
enddate=dt.date(year=2015,month=5,day=7)

totalfreq=[]
while not enddate==startdate:
    url='https://twitter.com/search?q=지진 since:'+str(startdate)+' until:'+str(untildate);#+'&amp;amp;amp;amp;amp;amp;lang=eg'
    browser.get(url)
    browser.implicitly_wait(10)

    html = browser.page_source
    soup=BeautifulSoup(html,'html.parser')
    
    lastHeight = 0
    newHeight = browser.execute_script("return document.body.scrollHeight")
    
    while lastHeight != newHeight:
        lastHeight = newHeight

        html = browser.page_source
        soup=BeautifulSoup(html,'html.parser')

        for item in soup.find_all("li", {"class": "stream-item"}):
            tweet = item.find('div', {"class":"tweet"})
            
            print('item-id',tweet['data-item-id'])
            print('data-name',tweet['data-name'])
            print('data-screen-name',tweet['data-screen-name'])
            print('data-user-id',tweet['data-user-id'])

            time_stamp = tweet.find("span",{"class":"_timestamp"})
            print('time-stamp', time_stamp['data-time'])
            print('text', tweet.find('p', {'class':'TweetTextSize'}).text)
        
        #아래로 내려
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        for i in range(0,6):
            browser.implicitly_wait(10)
            newHeight = browser.execute_script("return document.body.scrollHeight")
            if newHeight != lastHeight:
                break;

    # dailyfreq['Frequency']=wordfreq
    # wordfreq=0
    # totalfreq.append(dailyfreq)
    startdate=untildate
    untildate+=dt.timedelta(days=1)
    # dailyfreq={}

