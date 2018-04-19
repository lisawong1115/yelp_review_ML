# dataProcessor.py
# CS 232 final project
# Team: MLH
# author: Lisa Huang
# date: 04/12/18
# written in Python 2

import json
import re
import operator

nonspace = re.compile(r'\S')
def iterparse(j):
    decoder = json.JSONDecoder()
    pos = 0
    counter = 0 
    while True and counter<2000:
        matched = nonspace.search(j, pos)
        if not matched:
            break
        pos = matched.start()
        decoded, pos = decoder.raw_decode(j, pos)
        counter += 1
        yield decoded

def writeToJSON(filename, newFile):
    with open(filename, "r") as data_file:
        rawdata = data_file.read()

    data = []
    for decoded in iterparse(rawdata):
        data.append(decoded)
    # print("data length: (expected 100)" + str(len(data)))
    # j = json.dumps(data)
    with open(newFile, "w") as file:
        json.dump(data, file)

def sortBusiness(filename):
    with open(filename, "r") as file:
        data = json.load(file)
    result = {}
    for d in data:
        if d["business_id"] not in result:
            bID = d["business_id"]
            result[bID] = d["categories"]
    return result

def findCategories(businessDict):
    result = []
    for key in businessDict: #
        categories = businessDict[key]
        for category in categories:
            result.append(category)
    return list(set(result))

def frequencyOfCategories(reviewFile, businessFile):
    businessDict = sortBusiness(businessFile)
    categories = findCategories(businessDict)

    with open(reviewFile, "r") as f:
        reviews = json.load(f)

    frequencyDict = {}

    for category in categories:
        if category not in frequencyDict:
            frequencyDict[category] = 0

    for review in reviews:
        businessID = review["business_id"]
        if businessID in businessDict:
            categoriesOfOne = businessDict[businessID]

            for c in categoriesOfOne:
                frequencyDict[c] += 1

    return frequencyDict

def findBusinessByCategory(businessFile, category):
    businessDict = sortBusiness(businessFile)
    idList = []
    for key in businessDict:
        if category in businessDict[key]:
            idList.append(key)
    print("length of idList: " + str(len(idList)))
    return idList

def findReviewsByID(reviewFile, idList, outFile):
    with open(reviewFile, "r") as f:
        reviews = json.load(f)
    targets = []
    for review in reviews:
        if review["business_id"] in idList:
            targets.append(review)
    print("number of restaurant reviews: " + str(len(targets)))

    with open(outFile, "w") as file:
        json.dump(targets, file)

def getReviewLength(reviewFile):
    with open(reviewFile, "r") as f:
        reviews = json.load(f)
    distribution = {}
    for review in reviews:
        text = review["text"]
        length = len(text)
        if "character count" not in review:
            review["character count"] = length
        lowerRange = length/100*100
        lenRange = str(lowerRange) + "-" + str(lowerRange+100)
        if lenRange not in distribution:
            distribution[lenRange] = 1
        else:
            distribution[lenRange] += 1
    maximum = max(distribution.iteritems(), key=operator.itemgetter(1))
    return maximum

def reviewByLength(inFile, outFile):
    with open(inFile, "r") as f:
        data = json.load(f)
    reviews = []
    for review in data:
        text = review["text"]
        length = len(text)
        if "character count" not in review:
            review["character count"] = length
        if length >= 100 and length <=  200:
            reviews.append(review)
    with open(outFile, "w") as f:
        json.dump(reviews, f)
    return len(reviews)

def countVote(inFile):
    with open(inFile, "r") as f:
        data = json.load(f)
    # useful = []
    # useless = []
    result = {"useful": 0, "useless": 0}
    for review in data:
        if review["useful"] > 0:
            result["useful"] += 1
        else:
            result ["useless"] += 1
    return result

def splitFile(inFile, out1, out2):
    with open(inFile, "r") as f:
        data = json.load(f)
    useful = []
    useless = []
    for review in data:
        if review["useful"] > 0 and len(useful) < 130000:
            useful.append(review)
        elif review["useful"] == 0 and len(useless) < 130000:
            useless.append(review)

    with open(out1, "w") as f1:
        json.dump(useful, f1)
    with open(out2, "w") as f2:
        json.dump(useless, f2)
    return (len(useful), len(useless))


if __name__ == "__main__":
    # print(splitFile("restaurant_reviews_100-200.json", "useful.json", "useless.json"))

    # print(countVote("restaurant_reviews_100-200.json")) #{'useful': 139907, 'useless': 397023}
    # print(reviewByLength("restaurant_reviews.json", "restaurant_reviews_100-200.json"))

    # maximum = getReviewLength("restaurant_reviews.json")
    # print(maximum) #('100-200', 531573)

    # reviewFile = "reviewJSON.json"
    # idList = findBusinessByCategory("businessJSON.json", "Restaurants")
    # outFile = "restaurant_reviews.json"
    # findReviewsByID(reviewFile, idList, outFile)

    # d = frequencyOfCategories("reviewJSON.json", "businessJSON.json")
    # maximum = max(d.iteritems(), key=operator.itemgetter(1))
    # print(maximum) # (u'Restaurants', 3221419)

    # with open ("sample.json", "r") as f:
    #     d = json.load(f)
    #     newData = d["data"]
    # with open("new_review_sample.json", "w") as file:
    #     json.dump(newData, file)
    # writeToJSON("review.json", "reviewJSON.json")
    # print(len(categories))
    # writeToJSON(filename, "businessJSON.json")
    # with open ("businessCategories.json", "w") as file:
    #     json.dump(categories, file)
    # writeToJSON(filename, "newReviewTesting3.json")
    # divideData("newReviewTesting3.json", "vf2.json", "nf2.json")
