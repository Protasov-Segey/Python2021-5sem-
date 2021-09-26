#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import json
import csv
js = []
description = ["vitamin", "vitamers", "solubility", "daily_requirement", "deficiency_diseases"]
with open('A.txt') as v1, open('B6.txt') as v2, open('C.txt') as v3, open('D.txt') as v4, open('K.txt') as v5, open("vitamins.json", "w") as json_file :
    v1, v2, v3, v4, v5 = v1.readlines(), v2.readlines(), v3.readlines(), v4.readlines(), v5.readlines()
    for i in range(len(v1)-1):
        v1[i] = v1[i][:(len(v1[i]) - 1)]          
    for i in range(len(v2)-1):
        v2[i] = v2[i][:(len(v2[i]) - 1)] 
    for i in range(len(v3)-1):
        v3[i] = v3[i][:(len(v3[i]) - 1)]
    for i in range(len(v4)-1):
        v4[i] = v4[i][:(len(v4[i]) - 1)]
    for i in range(len(v5)-1):
        v5[i] = v5[i][:(len(v5[i]) - 1)]
    v1[1], v2[1], v3[1], v4[1], v5[1] = v1[1].split(', '), v2[1].split(', '), v3[1].split(', '), v4[1].split(', '), v5[1].split(', ')
    v1[4], v2[4], v3[4], v4[4], v5[4] = v1[4].split(', '), v2[4].split(', '), v3[4].split(', '), v4[4].split(', '), v5[4].split(', ')
    all_v = [v1, v2, v3, v4, v5]
    for i in range(len(description)) :
        d1 = {description[i] : v1[i] for i in range(len(description))}
        d2 = {description[i] : v2[i] for i in range(len(description))}
        d3 = {description[i] : v3[i] for i in range(len(description))}
        d4 = {description[i] : v4[i] for i in range(len(description))}
        d5 = {description[i] : v5[i] for i in range(len(description))}
    js.append(d1)
    js.append(d2)
    js.append(d3)
    js.append(d4)
    js.append(d5)
    json.dump(js, json_file)
print(json.dumps(js))
with open("vitamins.csv", "w") as csv_file:
    file_writer = csv.writer(csv_file)
    file_writer.writerow(description)
    file_writer.writerow(v1)
    file_writer.writerow(v2)
    file_writer.writerow(v3)
    file_writer.writerow(v4)
    file_writer.writerow(v5)
# в итоге мы имеем 2 файла: vitamins.csv и vitamins.json

