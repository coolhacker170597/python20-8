import os
import tempfile
import json
import argparse

##storage.py --key key_name --val value
parser = argparse.ArgumentParser()
parser.add_argument('--key')
##parser.add_argument('key_name')
parser.add_argument('--val')
##parser.add_argument('val_name')
key = parser.parse_args().key
val = parser.parse_args().val 
print(val, key)
storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
dic = dict()
with open(storage_path, 'w') as f:
    json.dump(dic, f)