#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

### train with 1% of data (optional)
# features_train = features_train[:len(features_train)/100]
# labels_train = labels_train[:len(labels_train)/100]

#########################################################
### your code goes here ###
from sklearn.svm import SVC
clf = SVC(C=10000.0 ,kernel='rbf')

t0 = time()
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"

t1 = time()
pred = clf.predict(features_test)
print "predicting time:", round(time()-t1, 3), "s"

print "accuracy:", clf.score(features_test, labels_test)

sara = 0
chris = 0
for i in pred:
	if (i == 0):
		sara += 1
	if (i == 1):
		chris += 1

print "Sara(0):", sara
print "Chris(1):", chris


### linear kernel ###
# training time: 135.267 s
# predicting time: 14.066 s
# accuracy: 0.984072810011

### linear kernel w/ 1% of data ###
# training time: 0.074 s
# predicting time: 0.776 s
# accuracy: 0.884527872582

### rbf kernel & C=1.0     w/ 1% of data ###
# training time: 0.081 s
# predicting time: 0.866 s
# accuracy: 0.616040955631

### rbf kernel & C=10.0    w/ 1% of data ###
# training time: 0.083 s
# predicting time: 0.879 s
# accuracy: 0.616040955631

### rbf kernel & C=100.0   w/ 1% of data ###
# training time: 0.083 s
# predicting time: 0.886 s
# accuracy: 0.616040955631

### rbf kernel & C=1000.0  w/ 1% of data ###
# training time: 0.078 s
# predicting time: 0.823 s
# accuracy: 0.821387940842

### rbf kernel & C=10000.0 w/ 1% of data ###
# training time: 0.077 s
# predicting time: 0.696 s
# accuracy: 0.892491467577

### rbf kernel & C=10000.0 ###
# training time: 89.014 s
# predicting time: 8.828 s
# accuracy: 0.990898748578
#########################################################


