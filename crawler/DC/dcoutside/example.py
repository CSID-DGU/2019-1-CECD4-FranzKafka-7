from dcoutside.crawler import DCInsideCrawler
from pprint import pprint
import json
import time
crawler = DCInsideCrawler()




to_json = []
i = 2
from_i = i
while(True):
    try:

        to_json.append(pprint(crawler.get_post('jijinhee', i)))
        time.sleep(3)
        if i%2000 == 0 :
            with open(str(from_i)+'_'+str(i)+'.json', 'w') as outfile:
                json.dump(to_json, outfile)
            to_json = []
            from_i = i+1
        i+=1
    except Exception as e:
        print(e)
        i+=1
        pass





