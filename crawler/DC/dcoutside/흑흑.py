from dcoutside.crawler import DCInsideCrawler
from pprint import pprint
import json
import time
import sys
import json
crawler = DCInsideCrawler()

gall_list=[]

with open('gall_list.json') as json_file:
    gall_list = json.load(json_file)
