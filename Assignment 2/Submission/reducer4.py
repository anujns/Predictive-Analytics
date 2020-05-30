#!/usr/bin/python3
import sys

input1 = {}
input2 = {}

for row in sys.stdin:
    row = row.strip()
    eID, name, salary, country, passcode = row.split('\t')

    if country == "NA":
        input1[eID] = name
    else:
        input2[eID] = [salary,country,passcode]

for key in input1.keys():
    name = input1[key]
    
    salary = input2[key][0]
    country = input2[key][1]
    passcode = input2[key][2]

    print ('{}\t{}\t{}\t{}\t{}'.format(key,name,salary,country,passcode))
