# -*- coding: utf-8 -*-
from selenium import webdriver
from util.extractor import *
import pdb
import time


if __name__ == "__main__":
    try:
        start_time = time.time()
        browser = CrawlBrowser(int(input()))
        browser.go_album()


        while(True):
            browser.go_next()
            browser.get_data_from_thumb()

        print(time.time()-start_time)


    except:
        print("error")
    finally:

        print("end")
