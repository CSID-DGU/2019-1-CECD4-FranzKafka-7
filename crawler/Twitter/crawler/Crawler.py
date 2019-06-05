#!/usr/bin/python3
import sns_data
import sys



if __name__ == "__main__":
    try:
        total_t = float(sys.argv[1])*60
        browser = sns_data.CrawlBrowser(total_t)
        browser.crawl_data()
        
        
    except Exception as ex:
        print("~~~~!!!! : ", ex)
    finally:
        print("end")
