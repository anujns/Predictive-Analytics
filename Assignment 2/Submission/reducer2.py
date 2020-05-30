#!/usr/bin/python3
import sys
import string
import operator
c = {}

for w in sys.stdin:

	word=w.split()
	if word[0] in c:
		c[word[0]]+=1
	else:
		c[word[0]]=1

d = dict(sorted(c.items(), key=operator.itemgetter(1),reverse=True))

for i, (k, v) in enumerate(d.items()):
    print('%s\t-->\t%s'%(k, v))
    if i > 8:
        break
