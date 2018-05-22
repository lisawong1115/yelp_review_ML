# play_with_model.py
# CS 232 Final Project
# Team MLH
# Author: Lisa Huang, Huihan Li
# Since: 2018/04/18
# Written in: Python 3 (but works fine with Python 2)
# Modified: 2018/04/29

import json
import re
import operator
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.feature_selection import SelectPercentile, f_classif
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
import numpy as np
from sklearn.model_selection import KFold, StratifiedKFold
from sklearn import preprocessing
from random import shuffle

"""
Using Multinomial Naive Bayes classifier from scikitlearn as well as the k-fold method, find an accuracy of prediction
at 54.5 percent
Only able to train test the classifier using 15000 "useful" reviews and 15000 "useless" reviews because processing more reviews
would cause MemoryError

A pilot stuy. Abandoned.
"""

def load_json(filename):
	with open(filename, "r") as f:
		data = json.load(f)
		f.close()
	return data[:15000]


if __name__ == "__main__":
	reviews = shuffle(load_json("useful650000.json")) + shuffle(load_json("useless650000.json"))
	labels = ["useful"] * 15000 + ["useless"] * 15000

	clf = MultinomialNB()
	accuracy = []

	kf = KFold(n_splits=10, shuffle=True)
	for train, test in kf.split(reviews):
		# both train, test are ndarrays
		X = np.reshape(reviews, (-1,1))
		# bag-of-words model, with stop words removed
		vectorizer = CountVectorizer(stop_words="english")
		features = vectorizer.fit_transform(reviews).toarray()
		y = np.array(labels)

		X_train, X_test, y_train, y_test = features[train], features[test], y[train], y[test]
		print(X_train)

		clf.fit(X_train, y_train)
		print("classifier fit.")

		pred = clf.predict(X_test)
		print("classfier predicted.")
		score = accuracy_score(pred, y_test)
		accuracy.append(score)
		print(score)

	print(accuracy)
	print(np.average(accuracy))
