import json
import os
import tempfile
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--key')
parser.add_argument('--val')
key = parser.parse_args().key
val = parser.parse_args().val

storage_path = os.path.join(tempfile.gettempdir(), '2.txt')

with open(storage_path, 'a+') as f:
    f.write(json.dumps({}))

with open(storage_path, 'w+') as storage_file:
    dic = json.loads(storage_file.read())

with open(storage_path, 'a+') as storage_file:
    print(dic)
    if val != None:
        if  key in dic:
            dic.update({key:dic[key]+', '+ val}) 
            print(dic, '1')
        else:
            dic.update({key:val}) 
            print(dic, '2')
        storage_file.write(json.dumps(dic))          
    else:        
        if key in dic:
            print(dic[key])
        else:
            print('None')
print(dic)



