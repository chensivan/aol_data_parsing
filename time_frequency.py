#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 08:38:11 2018

@author: yanchenm
"""

import csv
from datetime import datetime
import matplotlib.pyplot as plt

freq_over_time = open('freq_over_time_imperfect.csv', 'w')
freq_over_time_writer = csv.writer(freq_over_time)

x = '2006-03-10 11:58:51'
if datetime.strptime(x, '%Y-%m-%d %H:%M:%S') < datetime(2006, 3, 11):
    print('a')
else:
    print()
    

time_slot = {
        '3/1-3/10': 0,
        '3/11-3/20': 0,
        '3/21-3/31': 0,
        '4/1-4/10': 0,
        '4/11-4/20': 0,
        '4/21-4/30': 0,
        '5/1-5/10': 0,
        '5/11-5/20': 0,
        '5/21-5/31': 0
        }

word_time_freq = {}


with open('non_perfect.csv', 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader: 
        if len(row) > 0 and row[0] != 'AnonID':
            if row[1] not in word_time_freq:
                word_time_freq[row[1]] = {}
                word_time_freq[row[1]]['overall_freq'] = 0
                word_time_freq[row[1]]['time_slot'] = {
                                                        '3/1-3/10': 0,
                                                        '3/11-3/20': 0,
                                                        '3/21-3/31': 0,
                                                        '4/1-4/10': 0,
                                                        '4/11-4/20': 0,
                                                        '4/21-4/30': 0,
                                                        '5/1-5/10': 0,
                                                        '5/11-5/20': 0,
                                                        '5/21-5/31': 0
                                                        }
            word_time_freq[row[1]]['overall_freq'] += 1
            x = datetime.strptime(row[2], '%Y-%m-%d %H:%M:%S')
            if x > datetime(2006, 3, 1) and x < datetime(2006, 3, 11):
                word_time_freq[row[1]]['time_slot']['3/1-3/10'] += 1
            elif x > datetime(2006, 3, 11) and x < datetime(2006, 3, 21):
                word_time_freq[row[1]]['time_slot']['3/11-3/20'] += 1
            elif x > datetime(2006, 3, 21) and x < datetime(2006, 4, 1):
                word_time_freq[row[1]]['time_slot']['3/21-3/31'] += 1
            elif x > datetime(2006, 4, 1) and x < datetime(2006, 4, 11):
                word_time_freq[row[1]]['time_slot']['4/1-4/10'] += 1
            elif x > datetime(2006, 4, 11) and x < datetime(2006, 4, 21):
                word_time_freq[row[1]]['time_slot']['4/11-4/20'] += 1
            elif x > datetime(2006, 4, 21) and x < datetime(2006, 5, 1):
                word_time_freq[row[1]]['time_slot']['4/21-4/30'] += 1
            elif x > datetime(2006, 5, 1) and x < datetime(2006, 5, 11):
                word_time_freq[row[1]]['time_slot']['5/1-5/10'] += 1
            elif x > datetime(2006, 5, 11) and x < datetime(2006, 5, 21):
                word_time_freq[row[1]]['time_slot']['5/11-5/20'] += 1
            elif x > datetime(2006, 5, 21) and x < datetime(2006, 6, 1):
                word_time_freq[row[1]]['time_slot']['5/21-5/31'] += 1

i = 1
for key, value in sorted(word_time_freq.items(), key=lambda x: (x[1]['overall_freq']), reverse=True):
    row = [i, key, value['overall_freq']]
    val = list(value['time_slot'].values())
    i += 1
    freq_over_time_writer.writerow(row+val)


t100_freq_over_time = open('t100_freq_over_time_imperfect.csv', 'w')
t100_freq_over_time_writer = csv.writer(t100_freq_over_time)
i = 1
for key, value in sorted(word_time_freq.items(), key=lambda x: (x[1]['overall_freq']), reverse=True)[:100]:
    row = [i, key, value['overall_freq']]
    val = list(value['time_slot'].values())
    i += 1
    t100_freq_over_time_writer.writerow(row+val)


                
                