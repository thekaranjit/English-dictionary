# Python english dictionary

import json

data = json.load(open("data.json"))

def translate(word):
    print(data[word])
    



word = input("Please input the word to search the meaning: ")

translate(word)
#print(data["rain"])

