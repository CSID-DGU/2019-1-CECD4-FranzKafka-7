#!/usr/bin/python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from db import *
import datetime as dt
from bs4 import BeautifulSoup
import time
REDUNDANCY = 20.0
class CrawlBrowser:
    # browser = None
    # option = None
    def __init__(self, total_t):
        print('init')
        self.total_t = total_t
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('window-size=1920x1080')
        options.add_argument("disable-gpu")
        self.browser = webdriver.Chrome('chromedriver', chrome_options=options)

        self.url = "https://www.twitter.com/search?q=%s since:%s until:%s"
        
        self.keywords = Keyword.get()
        self.keyword = self.keywords[0]
        self.end_date = self.keyword['end_date']
        self.until = Sns.last_date(self.keyword['id'])
        self.since = self.until - dt.timedelta(days=1)

    def __del__(self):
        try:
            self.browser.close()
        except Exception as ex: 
            print('err:', ex)
        conn.close()
        cursor.close()

    def crawl_data(self):
        start_t = time.time()
        while self.until != self.end_date:
            print('crawl_data')
            self.go_twit()

            sns_list, twitter_metadata_list = self.main_loop()
            
            if sns_list != []:
                first_id = Sns.save(sns_list);

                TwitterMetadata.save(first_id, twitter_metadata_list)
            
            end_t = time.time()
            print(end_t-start_t,'s after')
            if end_t - start_t > self.total_t - REDUNDANCY:
                break;
            elif self.until == self.end_date:
                if len(keywords)-1 == keywords.index(keyword):
                    conn.close()
                    self.browser.close()
                    
                else:
                    self.keyword = self.keyword[keywords.index(keyword)+1]
            else:
                self.until = self.since
                self.since = self.until - dt.timedelta(days=1)




    def go_twit(self):
        print('go_twit')
        
        url = self.url%(self.keyword['word'], self.since, self.until)
        self.browser.get(url)
        self.browser.implicitly_wait(30)


    def main_loop(self):
        
        
        print('main_loop')
        keyword = self.keyword
        lastHeight = 0
        newHeight = self.browser.execute_script("return document.body.scrollHeight")

        sns_list = []
        twitter_metadata_list = []
        while lastHeight != newHeight:
            
            lastHeight = newHeight
            self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            for i in range(0,6):
                time.sleep(1)
                newHeight = self.browser.execute_script("return document.body.scrollHeight")
                if newHeight != lastHeight:
                    break;

        html = self.browser.page_source
        soup = BeautifulSoup(html,'html.parser')
        for item in soup.find_all("li", {"class": "stream-item"}):
                tweet = item.find('div', {"class":"tweet"})
                
                time_stamp = dt.datetime.fromtimestamp(int(tweet.find("span",{"class":"_timestamp"})['data-time']))
                content = tweet.find('p', {'class':'TweetTextSize'}).text
                sns_list.append((keyword['id'], content, str(time_stamp) ))
                
                twitter_metadata_list.append((tweet['data-item-id'], tweet['data-name'], tweet['data-screen-name'], tweet['data-user-id']))
        
        
        return sns_list, twitter_metadata_list


