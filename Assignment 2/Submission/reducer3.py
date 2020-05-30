#!/usr/bin/python3
import sys
c={}
for inp in sys.stdin:
	inp=inp.strip('\n')
	k,v=inp.split('\t',1)
	if k in c:
		c[k].append(v)
	else:
		c[k]=[]
		c[k].append(v)
for i in c:
	
	print ('%s\t----->\t%s'%(i,set(c[i])))
