# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 10:21:56 2016

@author: daukes
"""

import os
import csv
import yaml

a = 'courses.csv'
b = './'
c = os.path.normpath(os.path.join(b,a))

with open(c) as f:
    d = csv.reader(f)
    keys = d
    rows = [item for item in d]

entries = []
keys = rows[0]
#short_keys = ['time','name','title','email','school','description','tags','other_keywords','lab_name','lab_link','lab_description','lab_school','asu_unique','proud_of','personal_website_goals','external_communication','internal_communication','username']
keys = [key.replace(' ','-') for key in keys]
for row in rows[1:]:
    entry = dict([(key,value) for key,value in zip(keys,row)])
    print(entry)
    entries.append(entry)

filtered_keys = []
#filtered_keys = ['name','title','email','school','description','tags','other_keywords','lab_name','lab_link','lab_description','lab_school']
#filtered_keys = set(keys)-set(filtered_keys)
for entry in entries:
    for key in filtered_keys:
        entry.pop(key)
#    if not entry['lab_link'].startswith('http://'):
#        entry['lab_link'] = 'http://'+entry['lab_link']
#    entry['image']='/assets/images/asu_logo.svg'
#    entry['tags'] = [item.strip(' ') for item in entry['tags'].split(',')]
#    entry['image'] = '/assets/images/aukes-headshot.jpg'
#    entry['lab_image'] = '/assets/images/aukes-lab.jpg'
#    
file_structure = {}
file_structure['courses']=entries
with open('output2.yaml', 'w') as f:
    yaml.dump(file_structure,f)
