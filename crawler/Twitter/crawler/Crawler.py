# -*- coding: utf-8 -*-
import time
import sns_data


if __name__ == "__main__":
    try:
        
        start_time = time.time()
        browser = sns_data.CrawlBrowser()
        
        browser.crawl_data()
        
    except:
        browser.배고파()
        print("error")
    finally:
        print("end")
