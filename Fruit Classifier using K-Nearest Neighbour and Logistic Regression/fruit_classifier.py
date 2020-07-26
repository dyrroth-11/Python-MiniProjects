#!/usr/bin/env python3
"""
Created on Thu Apr 23 14:23:21 2020

@author: Ashish Patel
"""
"""
Problem: (a)We have to train a classifier to distinguish between different types of fruits using K-
            Nearest Neighbour and Logistic Regression.
         (b)Present in both of them which algorithm works better.
         (c)Visualize the training data and classified data using matplotlib.

"""
import matplotlib.cm as cm
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from matplotlib.colors import ListedColormap, BoundaryNorm
import matplotlib.patches as mpatches
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier

fruits = pd.read_table('dataset.txt')


# Training the classifier:
X_train, X_test, y_train, y_test = train_test_split(X,y,random_state=0)
scaler = MinMaxScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


# logistic Regression:
logreg = LogisticRegression()
logreg.fit(X_train, y_train)
print('****** Using logistic Regression ******')
print('Accuracy of Logistic regression classifier on training set: {:.2f}'.format(logreg.score(X_train, y_train)))
print('Accuracy of Logistic regression classifier on test set: {:.2f}\n\n'.format(logreg.score(X_test, y_test)))


# K-neareast Neighbour:
knn = KNeighborsClassifier()
knn.fit(X_train, y_train)
print('****** Using K-neareast Neighbour ******')
print('Accuracy of K-neareast Neighbour classifier on training set: {:.2f}'.format(knn.score(X_train, y_train)))
print('Accuracy of K-neareast Neighbour classifier on test set: {:.2f}\n\n'.format(knn.score(X_test, y_test)))


# Visualizing the data
X=fruits[['mass', 'width', 'height', 'color_score']]
y=fruits['fruit_label']
X_train, X_test, y_train, y_test = train_test_split(X,y,random_state=0)
def plot_fruit_knn(X, y, n_neighbors, weights):
    X_mat = X[['height', 'width']].values
    y_mat = y.values
    cmap_light = ListedColormap(['lightgreen', 'orange', 'pink', 'silver'])
    cmap_bold = ListedColormap(['red', 'green', 'yellow', 'grey'])
    clf = KNeighborsClassifier(n_neighbors, weights=weights)
    clf.fit(X_mat, y_mat)
    msize = .01
    psize = 50
    x_min, x_max = X_mat[:, 0].min() - 1, X_mat[:, 0].max() + 1
    y_min, y_max = X_mat[:, 1].min() - 1, X_mat[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, msize), np.arange(y_min, y_max,msize))
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    plt.figure()
    plt.pcolormesh(xx, yy, Z, cmap=cmap_light)
    plt.scatter(X_mat[:, 0], X_mat[:, 1],s=psize,c=y,cmap=cmap_bold,edgecolor='black')
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())
    p1 = mpatches.Patch(color='red', label='apple')
    p2 = mpatches.Patch(color='green', label='mandarin')
    p3 = mpatches.Patch(color='yellow', label='orange')
    p4 = mpatches.Patch(color='grey', label='lemon')
    plt.legend(handles=[p1,p2,p3,p4])
    plt.xlabel('height (in cm)')
    plt.ylabel('width (in cm)')
    plt.title("Classification on basis of height and width with same weight")
    plt.show()

plot_fruit_knn(X_train, y_train, 5, 'uniform')