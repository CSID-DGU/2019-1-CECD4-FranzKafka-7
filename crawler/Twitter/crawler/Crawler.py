#!/usr/bin/python3
import time
import sns_data
import os
import sys

if __name__ == "__main__":
    try:
        sys.path.append(os.path("/home/ubuntu/.local/lib/python3.5/site-packages"))
        start_time = time.time()
        browser = sns_data.CrawlBrowser()
        
        browser.crawl_data()
        
    except:
        browser.hungry()
        print("error")
    finally:
        browser.hungry()
        print("end")
