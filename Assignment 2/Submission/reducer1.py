#!/usr/bin/python3
import sys
count={}

for w in sys.stdin:
	
	word,value=w.split('\t',1)
	
	if word in count:
		count[word]=count[word]+1
	else:
		count[word]=int(value)
for j in count:
	print ('%s\t----->\t%s'%(j,count[j]))
