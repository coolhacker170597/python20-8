import os
import tempfile
import json
import argparse

##storage.py --key key_name --val value
parser = argparse.ArgumentParser()
parser.add_argument('--key')
parser.add_argument('--val')
key = parser.parse_args().key
val = str(parser.parse_args().val) 
storage_path = os.path.join(tempfile.gettempdir(), '2.json')
dic = dict()

if not os.path.exists(storage_path):
    with open(storage_path, 'w') as f:
        dic = {}
else:
    with open(storage_path, 'r+') as f:
        raw_data = f.read()
        if raw_data:
            dic = json.loads(raw_data)

with open(storage_path, 'r+') as f:    
    if val != 'None':        
        if  key in dic:
            dic.update({key:dic[key]+', '+ val}) 
        else:
            dic.update({key:val}) 
        f.write(json.dumps(dic, ensure_ascii=False))          
    else:        
        if key in dic:
            print(dic[key])
        else:
            print('None')