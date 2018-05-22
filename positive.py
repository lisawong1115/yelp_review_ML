# positive.py
# CS 232 final project
# Team: MLH
# author: Lisa Huang
# date: 05/09/18
# supported by Python 2 and 3

"""
A Python script that stores positive opinion words from positive-words.txt in a dictionary
"""

# a dictionary that stores all positive words from positive-words.txt
positive_dict = {}

with open("positive-words.txt", "r", encoding = "ISO-8859-1") as f:
	data = f.read().splitlines()
	for line in data:
		# ignoring the headers
		if len(line) > 0 and line[0] != ";":
			if line not in positive_dict:
				positive_dict[line] = 1

# print(len(positive_dict))
# print(positive_dict)