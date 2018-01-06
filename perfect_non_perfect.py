import csv
import string
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
import re
# find perfect query
pre_query = ''
temp = ''
sections = []
perfect_query = open('perfect.csv', 'w')
non_perfect_query = open('non_perfect.csv','w')
perfect_query_writer = csv.writer(perfect_query)
non_perfect_query_writer = csv.writer(non_perfect_query)



def remove_url_phone_query(sentence):
    sentence = sentence.lower()
    urls = re.findall('(http:\/\/www\.|https:\/\/www\.|http:\/\/|https:\/\/)?[a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,5}(:[0-9]{1,5})?(\/.*)?', sentence)
    phones = re.findall('(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})', sentence)
    return len(phones) + len(urls)

count = -1
counter = 0

#with open('data/test1.txt', 'r') as csvfile:
#    for lines in csvfile:
#        row = lines.split('\t')
#        print(row)
##   
#    
for i in range(10):
    print(str(i+1)+'a')

#a = open('test1.txt', 'r')
#csvReader = csv.reader(a)
#
#for lines in csvReader:
#    print(lines[0].split('\t'))
for i in range(10):
    if i < 9:
        file_name = 'data/data_txt/user-ct-test-collection-0'+str(i+1)+'.txt'
    else:
        file_name = 'data/data_txt/user-ct-test-collection-10.txt'
        
    with open(file_name, 'r') as csvfile:
    #    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        csvReader = csv.reader(csvfile)
        for lines in csvReader: 
            row = lines[0].split('\t')
            if row[0] != '' and remove_url_phone_query(row[1]) == 0:
                non_perfect_flag = 0
                if pre_query == row[1]:
                    if temp is not '':
                        sections.append(temp)
                        temp = ''
                    sections.append(row)
                else:
                    if len(sections) == 0:
                        count += 1
                        if len(temp) > 2 and temp[3] is not '':
                            perfect_query_writer.writerow(temp)
                        else:
                            non_perfect_query_writer.writerow(temp)
                    else:
                        count += len(sections)
                        itemRank = sections[0][3]
                        flag = 0
                        
                        for i in sections:
                            if itemRank != i[3]:
                                flag = 1
                                break
                        if flag == 0 and itemRank != '':
                            perfect_query_writer.writerows(sections)
                            non_perfect_flag = 1
                        else:
                            non_perfect_query_writer.writerows(sections)
                    
                    temp = row
                    sections = []
                    pre_query = row[1]
        
        if row[0] != '' and remove_url_phone_query(row[1]) == 0:  
            if len(sections) == 0:
                count += 1
                if len(temp) > 2 and temp[3] is not '':
                    perfect_query_writer.writerow(temp)
                else:
                    non_perfect_query_writer.writerow(temp)
            else:
                count += len(sections)
                itemRank = sections[0][3]
                flag = 0
                
                for i in sections:
                    if itemRank != i[3]:
                        flag = 1
                        break
                if flag == 0 and itemRank != '':
                    perfect_query_writer.writerows(sections)
                    non_perfect_flag = 1
                else:
                    non_perfect_query_writer.writerows(sections)
        
        print(count)
    origin_file = open(file_name)
    print(len(origin_file.readlines()))

perfect_file = open('perfect.csv')
non_perfect_file = open('non_perfect.csv')


print(len(perfect_file.readlines()))
print(len(non_perfect_file.readlines()))