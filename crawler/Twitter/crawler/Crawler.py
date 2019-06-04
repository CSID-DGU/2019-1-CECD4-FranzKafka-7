#!/usr/bin/python3
import sns_data


if __name__ == "__main__":
    try:
        browser = sns_data.CrawlBrowser()        
        browser.crawl_data()
        
    except:
        browser.hungry()
        print("error")
    finally:
        browser.hungry()
        print("end")
