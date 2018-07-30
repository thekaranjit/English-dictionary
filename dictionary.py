# Python english dictionary

import json
import difflib
from difflib import SequenceMatcher

from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:

        return data[word]

    else:
        return "The word doesnt exist. Please Try Again"






word = input("Please input the wsexord to search the meaning: ")

print(translate(word))
#print(data["rain"])

