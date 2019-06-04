#!/usr/bin/python3
import os
import sys
sys.path.append(os.path("/home/ubuntu/.local/lib/python3.5/site-packages"))
import time
import sns_data


if __name__ == "__main__":
    try:
        
        start_time = time.time()
        browser = sns_data.CrawlBrowser()
        
        browser.crawl_data()
        
    except:
        browser.hungry()
        print("error")
    finally:
        browser.hungry()
        print("end")
