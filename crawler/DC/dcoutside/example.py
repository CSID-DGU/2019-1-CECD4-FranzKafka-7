from dcoutside.crawler import DCInsideCrawler
from pprint import pprint
import json
import time
import sys
crawler = DCInsideCrawler()




to_json = []
i = int(sys.argv[1])
end = int(sys.argv[2])
from_i = i
while(True):
    try:

        to_json.append(pprint(crawler.get_post('jijinhee', i)))
        time.sleep(6)
        if i%100 == 99 or i == end :
            with open(str(from_i)+'_'+str(i)+'.json', 'w') as outfile:
                json.dump(to_json, outfile)
            to_json = []
            from_i = i+1
        if i == end:
            break;
        i+=1
    except Exception as e:
        print(e)
        i+=1
        pass





