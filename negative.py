# negative.py
# CS 232 final project
# Team: MLH
# author: Lisa Huang
# date: 05/09/18
# supported by Python 2 and 3

"""
A Python script that stores negative opinion words from negative-words.txt in a dictionary
"""

# a dictionary that stores all negative words from negative-words.txt
negative_dict = {}
with open("negative-words.txt", "r", encoding = "ISO-8859-1") as f:
	data = f.read().splitlines()
	for line in data:
		# ignoring headers
		if len(line) > 0 and line[0] != ";":
			if line not in negative_dict:
				negative_dict[line] = 1


# print(len(negative_dict))
# print(negative_dict)
