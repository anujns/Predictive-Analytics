#!/usr/bin/python3
import sys
import string
import re
import os
for eachline in sys.stdin:
	file_id=os.path.basename(os.environ['map_input_file'])
	words_per_line=re.split(r'--|\s|,',eachline)
	
	for eachword in words_per_line:
		w=eachword.strip(string.punctuation).lower()
		word=w.strip('-—“”’')
		if(word!=""):
			print ('%s\t%s'%(word,file_id))
	
