# split_data.py
# CS 232 final project
# Team: MLH
# author: Lisa Huang
# date: 04/15/18
# written in Python 2

import json

def splitData(infile, trainFile, testFile, num):
	with open(infile, "r") as in_data:
		data = json.load(in_data)

	toTrain = []
	toTest = []

	for i in range(0, num):
		if i < num*0.8: # 5000*0.8 = 4000
			toTrain.append(data[i])
		else:
			toTest.append(data[i])

	with open(trainFile, "w") as train_data:
		json.dump(toTrain, train_data)

	with open(testFile, "w") as test_data:
		json.dump(toTest, test_data)


if __name__ == "__main__":
	noVote_toTrain = "nf_train.json"
	noVote_toTest = "nf_test.json"
	withVote_toTrain = "vf_train.json"
	withVote_toTest = "vf_test.json"

	noVote = "nf2.json"
	withVote = "vf2.json"

	splitData(noVote, noVote_toTrain, noVote_toTest, 5000)
	splitData(withVote, withVote_toTrain, withVote_toTest, 5000)


