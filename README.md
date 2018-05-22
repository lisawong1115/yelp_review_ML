# Yelp Review Predictor

## Lisa Huang, Huihan Li, Mara-Steiu Florina
## CS 232: Artificial Intelligence
## 22 May 2018
## Wellesley College

### raw files (in data.zip):
  * __useful650000.json__: 650,000 English reviews of restaurants with "useful" votes, with length of 100-599 characters
  * __useless650000.json__: 650,000 English reviews of restaurants without "useful" votes, with length of 100-599 characters
  * __businessJSON.json__: all businesses collected from Yelp Dataset Challenge
  * __positive-words.txt__: a list of POSITIVE opinion words
  * __negative-words.txt__: a list of NEGATIVE opinion words

### data processing files:
  * __dataProcessor.py__: a Python script that cleans the original 5 million review data based on certain conditions
  * __open_business.py__: a Python script that loads businessJSON.json
  * __open_useful_reviews.py__: a Python script that loads useful650000.json
  * __open_useless_reviews.py__: a Python script that loads useless650000.json
  * __positive.py__: a Python script that stores positive opinion words from positive-words.txt in a dictionary
  * __negative.py__: a Python script that stores negative opinion words from negative-words.txt in a dictionary

### main file:
  * __play_with_model.py__: a pilot model that has an accuracy of prediction of 54.5%; abandoned
  * __Yelp_review_Predictor.ipynb__ : the main file that deals with data analysis and cleaning, finding language features, training and testing on the model, and predicting new reviews

### other file(s):
  * __frequency.txt__: the distribution of review lengths