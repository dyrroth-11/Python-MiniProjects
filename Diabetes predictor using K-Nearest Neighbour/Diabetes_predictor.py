#!/usr/bin/env python3
"""
Created on Thu Apr 23 16:12:37 2020

@author: Ashish Patel
"""
"""
Problem: (a)We have to predict whether the patient has diabetes or not based on various features given
            in the dataset .
         (b)Visualize the training data and classified data using matplotlib.

"""

#%matplotlib inline
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier


#reading data:
diabetes = pd.read_csv('dataset.csv')


# training this model using K-neareast Neighbour:
X_train, X_test, y_train, y_test = train_test_split(diabetes.loc[:, diabetes.columns != 'Outcome'], diabetes['Outcome'], stratify=diabetes['Outcome'], random_state=66)
training_accuracy = []
test_accuracy = []
neighbors_settings = range(1, 11)
for n_neighbors in neighbors_settings:
    knn = KNeighborsClassifier(n_neighbors=n_neighbors)
    knn.fit(X_train, y_train)
    training_accuracy.append(knn.score(X_train, y_train))
    test_accuracy.append(knn.score(X_test, y_test))


# Predicting the accuracy :
knn = KNeighborsClassifier(n_neighbors=9)
knn.fit(X_train, y_train)
print('****** Using K-neareast Neighbour ******')
print('Accuracy of K-neareast Neighbour classifier on training set: {:.2f}'.format(knn.score(X_train, y_train)))
print('Accuracy of K-neareast Neighbour classifier on test set: {:.2f}'.format(knn.score(X_test, y_test)))


# Visualizing the data:
plt.plot(neighbors_settings, training_accuracy, label="training accuracy")
plt.plot(neighbors_settings, test_accuracy, label="test accuracy")
plt.ylabel("Accuracy")
plt.xlabel("n_neighbors")
plt.legend()
plt.savefig('knn_compare_model')