# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 10:21:56 2016

@author: daukes
"""

import os
import csv
import yaml

a = 'images.csv'
b = './'
c = os.path.normpath(os.path.join(b,a))

with open(c) as f:
    d = csv.reader(f)
    keys = d
    rows = [item for item in d]

entries = []
keys = rows[0]
keys = [key.replace(' ','-') for key in keys]
for row in rows[1:]:
    entry = dict([(key,value) for key,value in zip(keys,row)])
    print(entry)
    entries.append(entry)

filtered_keys = []
for entry in entries:
    for key in filtered_keys:
        entry.pop(key)
#    
file_structure = {}
file_structure['images']=entries
with open('images.yaml', 'w') as f:
    yaml.dump(file_structure,f)
