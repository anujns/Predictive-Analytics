#!/usr/bin/python3
import sys
import numpy as np
from scipy import stats

joiner = {}

k = 10 

for rows in sys.stdin:
	cols = rows.split('\t')
	info = [cols[1], cols[2]]
	

	x = np.asarray(info)
	x = x.astype(np.float)
	x = x.reshape((1, x.shape[0]))
	if cols[0] in joiner:
		y = np.append(joiner[cols[0]], x, axis=0)
		joiner[cols[0]] = y
	else:
		joiner[cols[0]] = x



for items in joiner.keys():
	matrix = joiner[items]
	sorted_matrix = matrix[matrix[:,0].argsort()]
	sorted_matrix = sorted_matrix[:k]
	l = stats.mode(sorted_matrix[:,1])[0]
	print('{} {}'.format(items, str(list(l))))
	
