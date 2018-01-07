#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 09:54:09 2018

@author: yanchenm
"""



def overall_time_frequency():
    word_time_freq = {}
    word_time_freq = {
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
    with open('perfect.csv', 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader: 
        if len(row) > 0 and row[0] != 'AnonID':
            x = datetime.strptime(row[2], '%Y-%m-%d %H:%M:%S')
            if x > datetime(2006, 3, 1) and x < datetime(2006, 3, 11):
                word_time_freq['3/1-3/10'] += 1
            elif x > datetime(2006, 3, 11) and x < datetime(2006, 3, 21):
                word_time_freq['3/11-3/20'] += 1
            elif x > datetime(2006, 3, 21) and x < datetime(2006, 4, 1):
                word_time_freq['3/21-3/31'] += 1
            elif x > datetime(2006, 4, 1) and x < datetime(2006, 4, 11):
                word_time_freq['4/1-4/10'] += 1
            elif x > datetime(2006, 4, 11) and x < datetime(2006, 4, 21):
                word_time_freq['4/11-4/20'] += 1
            elif x > datetime(2006, 4, 21) and x < datetime(2006, 5, 1):
                word_time_freq['4/21-4/30'] += 1
            elif x > datetime(2006, 5, 1) and x < datetime(2006, 5, 11):
                word_time_freq['5/1-5/10'] += 1
            elif x > datetime(2006, 5, 11) and x < datetime(2006, 5, 21):
                word_time_freq['5/11-5/20'] += 1
            elif x > datetime(2006, 5, 21) and x < datetime(2006, 6, 1):
                word_time_freq['5/21-5/31'] += 1
                
     print(word_time_freq)         
                