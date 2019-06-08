from dcoutside.crawler import DCInsideCrawler
from pprint import pprint
import json
import time
import sys
crawler = DCInsideCrawler()


# save_list = []

# for i in range(1, 384):
#     time.sleep(3)
#     save_list += crawler.get_board_num('jijinhee',i)

# with open('gall_list.json', 'w') as outfile:
#     json.dump(save_list, outfile)
gall_list=[]

with open('gall_list.json') as json_file:
    gall_list = json.load(json_file)

size = len(gall_list)

start = int(sys.argv[1])
end = int(sys.argv[2])

crawling_list = gall_list[start:end]


to_json = []



from_val = crawling_list[0]

for idx, val in enumerate(crawling_list):
    try:
        time.sleep(3)
        tmp = crawler.get_post('jijinhee', int(val))
        pprint(tmp)
        to_json.append(tmp)

    except KeyboardInterrupt:
        print('keyboard interrupt')
        with open(str(from_val)+'_'+str(val)+'.json', 'w') as outfile:
            json.dump(to_json, outfile)

    except Exception as e:
        print(e)
        pass

    finally:
        if idx%300==299 or idx == size-1 :
            with open(str(from_val)+'_'+str(val)+'.json', 'w') as outfile:
                json.dump(to_json, outfile)
            to_json = []
            from_val = val





