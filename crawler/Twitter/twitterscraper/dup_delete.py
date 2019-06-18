import json
import sys
import os
path = sys.argv[1]

# with statement
with open(path) as json_file:
    json_data = json.load(json_file)


x = list({ json_datum['id']: json_datum for json_datum in json_data }.values())

print('원본 데이터 : ',str(len(json_data)))
print('지운 데이터 : ',str(len(x)))
origin_path = path
path = path[2:]
path = path[0:9] + path[11:]
with open('d_'+path, 'w') as outfile:
    json.dump(x, outfile)

os.system('mv '+str(origin_path)+' origin/'+str(origin_path))
os.system('ls')


# x = []
# for json_datum in json_data:
#     json_datum.pop('url')
#     json_datum.pop('html')
#     x.append(json_data)

# origin_path = path
# path = path[2:]
# with open(path, 'w') as outfile:
#     json.dump(x, outfile)

# os.system('rm '+str(origin_path))
# os.system('ls')
