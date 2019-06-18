import os

import datetime as dt


ed = dt.date(2018, 2, 6)
bd = ed - dt.timedelta(days=120)

command = "twitterscraper 지진 -bd %s -ed %s -o %s.json"

while(bd > dt.date(2006, 1, 1)):
    cm =  command%(str(bd), str(ed), str(bd)+'_'+str(ed))
    print(cm)

    os.system(cm)

    ed = bd
    bd = ed - dt.timedelta(days=120)
    
