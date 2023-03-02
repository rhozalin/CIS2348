# Name-Rhozalin Nath
# PS ID: 2050395
import csv
input=input()
with open(input, 'r') as wordsfile:
    reader = csv.reader(wordsfile)
    dict={}
    for row in reader:
        for word in row:
            dict[word]=row.count(word)

    for i in dict:
        print (f"{i} {dict[i]}")