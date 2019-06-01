# -*- coding: utf-8 -*-
from selenium import webdriver
import pdb;
import re;
import os;
from selenium.webdriver.common.keys import Keys
from db import *

class CrawlBrowser:
    # browser = None
    # option = None
    def __init__(self,num):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('window-size=1920x1080')
        options.add_argument("disable-gpu")

        self.browser = webdriver.Chrome('chromedriver', chrome_options=options)
        # self.resDict = {'media_id': [], 'img_url': [], 'review_url': [], 'display_date': [],'keyword':self.keyword}
        self.url = "https://www.twitter.com/"
        



    def go_album(self):
        print("go_album")
        self.browser.get(self.url+"/Search?uiOrigin=MASTHEAD&q="+self.keyword)
        print("url로 접속")
        self.browser.implicitly_wait(30)
        self.url+=self.browser.find_elements_by_xpath("//div[@class='result-title']//span[text()='"+self.keyword+"']/parent::*")[0].get_attribute("onclick").split("'")[3]
        self.browser.implicitly_wait(10)
        self.browser.get(self.url)
        self.browser.implicitly_wait(10)
        self.max_count = int(self.browser.find_elements_by_css_selector(".see_all_count")[0].get_attribute("textContent").replace(",",""))
        self.count_sql = '''
        SELECT count(image_idx) count from image_info where search_keyword=%s;
        '''

        # print (self.count_sql % keyword)
        self.cursor.execute(self.count_sql,self.keyword)
        count = int(self.cursor.fetchone()['count'])
        print("총"+str(self.max_count)+"개 "+str(count)+"개")

        self.browser.execute_script("ta.plc_resp_photo_mosaic_ar_responsive_0_handlers.openPhotoViewer();")
        print("앨범 클릭")
        self.browser.implicitly_wait(10)
        self.browser.find_elements_by_css_selector(".photoGridImg")[0].click()
        print("첫번째 사진 클릭")

        self.browser.implicitly_wait(10)

    def insert_data(self, trip_list, img_list):
        print("insert_data")
        self.cursor.executemany(self.trip_sql,trip_list)
        first_id = self.conn.insert_id()
        for idx , val in enumerate(range(first_id,first_id+len(img_list))):
            img_list[idx].append(val)
            img_list[idx].append(self.keyword)

        self.cursor.executemany(self.img_sql,img_list)
        self.cursor.connection.commit()


    def get_data_from_thumb(self):
        print("get_data_from_thumb")

        trip_list=[]
        img_list=[]

        for thumb in self.browser.find_elements_by_css_selector(".tinyThumb"):
            trip_list.append([thumb.get_attribute("data-mediaid"),thumb.get_attribute("data-reviewurl")])
            img_list.append([thumb.get_attribute("data-bigurl")])
        self.insert_data(trip_list,img_list)
        if len(self.browser.find_elements_by_css_selector(".tinyThumb"))<48:
            raise exceptions()




    def __del__(self):
        self.browser.close()
        print ("browser closed")
        self.cursor.close()


    def go_next(self):
        # pdb.set_trace()
        print("go_next")
        self.cursor.execute(self.count_sql,self.keyword)
        count = int(self.cursor.fetchone()['count'])
        print("총"+str(self.max_count)+"개 "+str(count)+"개")
        origin_url = self.browser.current_url

        sql = '''
        SELECT trip_metadata.trip_gallery_id
        from image_info LEFT JOIN trip_metadata
        on image_info.trip_idx=trip_metadata.trip_idx
        where search_keyword=%s
        order by trip_metadata.trip_idx desc limit 1;
        '''

        # print((sql % (self.keyword)).replace("\n"," "))
        if self.cursor.execute(sql,self.keyword)==1:
            last_media_id = self.cursor.fetchone()['trip_gallery_id']
            new_url = origin_url.replace(re.findall("\d+", origin_url)[-1], last_media_id)

            self.browser.get("https://www.tripadvisor.co.kr/")
            self.browser.get(new_url)
            print(new_url)
            self.browser.implicitly_wait(30)
