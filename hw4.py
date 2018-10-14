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
storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
dic = dict()
with open(storage_path, 'r', encoding = 'utf-8') as f:
    dic = json.load(f)
if val != 'None':
    with open(storage_path, 'w', encoding = 'utf-8') as f:         
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
