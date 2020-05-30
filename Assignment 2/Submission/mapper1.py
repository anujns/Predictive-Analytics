#!/usr/bin/python3
import sys
import string
import re

for eachline in sys.stdin:

	words_per_line=re.split(r'--|\s|,',eachline)
	
	for eachword in words_per_line:
		w=eachword.strip(string.punctuation).lower()
		word=w.strip('-—“”’')
		if(word!=""):
			print ('%s\t%s'%(word,1))
	
