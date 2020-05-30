#!/usr/bin/python3
import sys
import re
import string


for line in sys.stdin:

	words = line.split()
	words = re.findall(r'\w+', line.strip())
	length = len(words)
	i = 0
	while (i+2 < length):

		first = words[i]
		first = first.strip(string.punctuation).lower()

		second = words[i+1]
		second = second.strip(string.punctuation).lower()

		third = words[i+2]
		third = third.strip(string.punctuation).lower()


		tri_temp = [first, second, third]
		delim = '_'

		if (first == 'science' or first == 'sea' or first == 'fire' or first == 'sciences' or first == 'seas' or first == 'fires'):
			tri_temp = ['$', second, third]
			tri = delim.join(tri_temp)
			print(tri,1)
		elif (second == 'science' or second == 'sea' or second == 'fire' or second == 'sciences' or second == 'seas' or second == 'fires'):
			tri_temp = [first, '$', third]
			tri = delim.join(tri_temp)
			print(tri,1)
		elif (third == 'science' or third == 'sea' or third == 'fire' or third == 'sciences' or third == 'seas' or third == 'fires'):
			tri_temp = [first, second, '$']
			tri = delim.join(tri_temp)
			print(tri,1)
		i += 1
