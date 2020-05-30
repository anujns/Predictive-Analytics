#!/usr/bin/python3
import sys
import numpy as np
import pandas as pd

df = pd.read_csv('Test.csv')

for row in sys.stdin:
	row = row.strip()
	cols=row.split(',')

	np_array = np.asarray(cols)
	np_array = np_array.astype(np.float)
	np_array = np_array.reshape((1, np_array.shape[0]))
	np_data = np_array[:,:-1]
	np_label = np_array[:,-1]
	test_array = np.asarray(df.values)
	matrix = np.tile(np_data ,(test_array.shape[0],1))
	difference_matrix = np.sum(np.absolute(test_array - matrix), axis=1)
	for rw in range(len(test_array)):
		out = [str(difference_matrix[rw]), str(np_label[0])]
		print ('{}\t{}\t{}'.format(rw,difference_matrix[rw], np_label[0]))
