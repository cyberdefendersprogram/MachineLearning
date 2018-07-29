# Import packages needed
import os
import numpy as np
import pandas as pd
from sklearn import svm
from sklearn import preprocessing
import time

# This function builds training dataset and testing dataset
def Build_Data_Set():
	df = pd.read_csv('../Data/out.csv', index_col=0) 	# 100000 entries
	df_train = df[:50000] 	# Take last 50000 rows as a training dataset
	df_test = df[10000:]   # Take first 10000 rows as a testing dataset

	# Clean up training dataset and scale it
	X_train = np.array(df_train.drop(['classification','usage_counter', 'normal_prio', 'policy', 'vm_pgoff', 'task_size', 'cached_hole_size', 'hiwater_rss', 'nr_ptes', 'lock', 'cgtime', 'signal_nvcsw'], 1))
	X_train = preprocessing.scale(X_train)
	# Training label
	y_train = np.array(df_train['classification'].replace("malware",0).replace("benign",1))

	# Clean up testing dataset and scale it
	X_test = np.array(df_test.drop(['classification','usage_counter', 'normal_prio', 'policy', 'vm_pgoff', 'task_size', 'cached_hole_size', 'hiwater_rss', 'nr_ptes', 'lock', 'cgtime', 'signal_nvcsw'], 1))
	X_test = preprocessing.scale(X_test)
	#Testing label
	y_test = np.array(df_test['classification'].replace("malware",0).replace("benign",1))

	return X_train, X_test, y_train, y_test # Return arrays

# This function builds a machine learning model using scikit-learn svm algorithm and compute the Accuracy of the prediction
def Analysis():
	test_size = 10000 # The size of the testing dataset
	X_train, X_test, y_train, y_test = Build_Data_Set() # Building training and testing datasets

	clf = svm.SVC(kernel="linear", C=0.01) # Declare a svm object in with scikit-learn package 
	clf.fit(X_train, y_train) # Training the model with the traning dataset and labels
	result = clf.predict(X_test) # Running a prediction with 10000 samples

	# Compute the accuracy and print it out
	correct_count = 0
	for i in range(0,test_size):
		if result[i] == y_test[i]:
			correct_count += 1

	print("Accuracy:", (correct_count/test_size)*100)
	return


start = time.time()
Analysis() # run the program
end = time.time()

elapsed = end - start

print("Time:",elapsed)


# import sha3
# import hashlib
# # encoding GeeksforGeeks using md5 hash
# # function 
# df = pd.read_csv('new_data.csv', index_col=0) 	# 100000 entries

# # s = hashlib.sha3_512()
# # s.update(b"hello")
# # print(s.hexdigest())

# df['hash'] = df['hash'].apply(hash)
# df.to_csv('out.csv')
