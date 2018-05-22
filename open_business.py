# open_business.py
# CS 232 final project
# Team: MLH
# author: Lisa Huang
# date: 05/05/18
# supported by Python 2 and 3

"""
A Python script that loads businessJSON.json to avoid occupying a lot of memory.
"""

import json

with open("businessJSON.json", "r") as f:
	data = json.load(f)

businesses = list(data)