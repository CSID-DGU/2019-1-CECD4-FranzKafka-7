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
        time.sleep(3)
        if len(to_json) >= 100 or i == end :
            with open(str(from_i)+'_'+str(i-1)+'.json', 'w') as outfile:
                json.dump(to_json, outfile)
            to_json = []
            from_i = i

        pprint(crawler.get_post('jijinhee', i))

        to_json.append(crawler.get_post('jijinhee', i))

        if i == end:
            break;

        i+=1
    except KeyboardInterrupt:
        print('keyboard interrupt')
        with open(str(from_i)+'_'+str(i-1)+'.json', 'w') as outfile:
            json.dump(to_json, outfile)
            
            
    except Exception as e:
        print(e)
        i+=1
        pass





