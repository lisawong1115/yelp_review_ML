import json
import re

nonspace = re.compile(r'\S')
def iterparse(j):
    decoder = json.JSONDecoder()
    pos = 0
    counter = 0 
    while True and counter<20000:
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

    data = {"data": []}
    for decoded in iterparse(rawdata):
        data["data"].append(decoded)
    # print("data length: (expected 100)" + str(len(data)))
    # j = json.dumps(data)
    with open(newFile, "w") as file:
        json.dump(data, file)

def divideData(filename, voteFile, nvFile):
    with open(filename, "r") as json_data:
        d = json.load(json_data)
        json_data.close()
        # d["data"] is a list of dictionaries
    vCount = 0
    nCount = 0
    withVotes = []
    noVotes = []
    for dct in d["data"]:
        if dct[u"useful"] == 0 and dct[u"funny"] == 0 and dct[u"cool"] == 0 and nCount < 5000:
            noVotes.append(dct)
            nCount += 1
        else:
            if vCount < 5000:
                withVotes.append(dct)
                vCount += 1
    print("length of votes:" + str(len(withVotes)))
    print("length of noVotes:" + str(len(noVotes)))
    with open(voteFile, "w") as vf:
        json.dump(withVotes, vf)
    with open(nvFile, "w") as nf:
        json.dump(noVotes, nf)
    # print("Yeah")


if __name__ == "__main__":
    filename = "review.json"
    # writeToJSON(filename, "newReviewTesting3.json")
    # divideData("newReviewTesting3.json", "vf2.json", "nf2.json")
