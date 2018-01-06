#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 20:11:32 2018

@author: yanchenm
"""


from nltk import ne_chunk, pos_tag, word_tokenize
from nltk.tree import Tree
import csv
import string
#nltk.help.upenn_tagset('NNS')
from collections import Counter
from time import gmtime, strftime
#txt = " obama beijing how google to remove adware computer" 
#chunkated = pos_tag(word_tokenize(txt))
#counts = Counter(tag for word,tag in chunkated)
#
#print(chunkated)
#print(ne_chunk(pos_tag(word_tokenize(txt)), binary=True))
#print(counts)


def filt(x):
    return x.label()=='NE'

COUNT = 0

def get_NN_from_text(text):
#    chunked = ne_chunk(pos_tag(word_tokenize(text)), binary=True)
    chunkated = pos_tag(word_tokenize(text))
    counts = Counter(tag for word,tag in chunkated)
    global COUNT
    COUNT = COUNT+1
    if COUNT % 100000 == 0:
        print(strftime("%Y-%m-%d %H:%M:%S", gmtime()))

    num_entity = 0
#    for subtree in chunked.subtrees(filter =  filt): # Generate all subtrees
#        num_entity += 1
    if 'NN' in counts:
        num_entity += counts['NN']
    if'NNP' in counts:
        num_entity += counts['NNP']
    if'NNS' in counts:
        num_entity += counts['NNS']
    
    return num_entity
    
#get_NN_from_text('showcase cinamas')


single_entity = open('single_entity.csv','w')
single_entity_writer = csv.writer(single_entity)
double_entity = open('double_entity.csv', 'w')
double_entity_writer = csv.writer(double_entity)
triple_entity = open('triple_entity.csv', 'w')
triple_entity_writer = csv.writer(triple_entity)

import csv
word_fre = {}
word_fre_single = {}
word_fre_double = {}
word_fre_triple = {}

with open('non_perfect.csv', 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader: 
        if len(row) > 0 and row[0] != 'AnonID':
            if row[1] not in word_fre:
                word_fre[row[1]] = {}
                word_fre[row[1]]['freq'] = 0
                word_fre[row[1]]['ids'] = set()
                
            word_fre[row[1]]['freq'] += 1

            word_fre[row[1]]['ids'].add(row[0])  
print(len(word_fre.keys()))           
single_entity_writer.writerow(['Rank', 'Query', 'Frequency', '# of user ID'])
double_entity_writer.writerow(['Rank', 'Query', 'Frequency', '# of user ID'])
triple_entity_writer.writerow(['Rank', 'Query', 'Frequency', '# of user ID'])

                               
for key, value in word_fre.items():
    value['num_user'] = len(value['ids'])
    value['freqPerUser'] = len(value['ids']) / value['freq'] 
    num_entity = get_NN_from_text(key)
    if num_entity == 1:
        word_fre_single[key] = word_fre[key]
    elif num_entity == 2:
        word_fre_double[key] = word_fre[key]
    elif num_entity == 3:
        word_fre_triple[key] = word_fre[key]
#    print(num_entity, key)
#    row = [i, key, value['freq'], value['num_user']]
#    print(row)
#    top100_perfect_writer.writerow(row)


i = 1
print('single entity')
for key, value in sorted(word_fre_single.items(), key=lambda x: (x[1]['freq'], x[1]['num_user']), reverse=True)[:100]:
#    print (i, key, value)
    row = [i, key, value['freq'], value['num_user']]
    print(row)
    single_entity_writer.writerow(row)
    i += 1


i = 1
print('double entity')
for key, value in sorted(word_fre_double.items(), key=lambda x: (x[1]['freq'], x[1]['num_user']), reverse=True)[:100]:
#    print (i, key, value)
    row = [i, key, value['freq'], value['num_user']]
    print(row)
    double_entity_writer.writerow(row)
    i += 1



i = 1
print('triple entity')
for key, value in sorted(word_fre_triple.items(), key=lambda x: (x[1]['freq'], x[1]['num_user']), reverse=True)[:100]:
#    print (i, key, value)
    row = [i, key, value['freq'], value['num_user']]
    print(row)
    triple_entity_writer.writerow(row)
    i += 1




#
#def get_continuous_chunks(text):
#    chunked = ne_chunk(pos_tag(word_tokenize(text)))
#    prev = None
#    continuous_chunk = []
#    current_chunk = []
#
#    for i in chunked:
#        if type(i) == Tree:
#            current_chunk.append(" ".join([token for token, pos in i.leaves()]))
#        elif current_chunk:
#            named_entity = " ".join(current_chunk)
#            if named_entity not in continuous_chunk:
#                continuous_chunk.append(named_entity)
#                current_chunk = []
#        else:
#            continue
#    if current_chunk:
#        named_entity = " ".join(current_chunk)
#        if named_entity not in continuous_chunk:
#            continuous_chunk.append(named_entity)
#            current_chunk = []
#    return continuous_chunk

