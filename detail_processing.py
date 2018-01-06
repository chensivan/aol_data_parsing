#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 16:04:17 2017

@author: yanchenm
"""

import csv
import string
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
import re

from collections import Counter
import numpy as np
import matplotlib.pyplot as plt



top100_non_perfect = open('top100_perfect.csv','w')
top100_perfect_writer = csv.writer(top100_non_perfect)


import csv
word_fre = {}


with open('perfect.csv', 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader: 
        if len(row) > 0 and row[0] != 'AnonID':
            if row[1] not in word_fre:
                word_fre[row[1]] = {}
                word_fre[row[1]]['freq'] = 0
                word_fre[row[1]]['ids'] = set()
                
            word_fre[row[1]]['freq'] += 1

            word_fre[row[1]]['ids'].add(row[0])  


top100_perfect_writer.writerow(['Rank', 'Query', 'Frequency', '# of user ID'])

for key, value in word_fre.items():
    value['num_user'] = len(value['ids'])
    value['freqPerUser'] = len(value['ids']) / value['freq'] 
#    row = [i, key, value['freq'], value['num_user']]
#    print(row)
#    top100_perfect_writer.writerow(row)

i = 1
for key, value in sorted(word_fre.items(), key=lambda x: (x[1]['freq'], x[1]['num_user']), reverse=True)[:100]:
#    print (i, key, value)
    row = [i, key, value['freq'], value['num_user']]
    print(row)
    top100_perfect_writer.writerow(row)
    i += 1


