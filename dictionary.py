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

    elif len(get_close_matches(word, data.keys())) > 0:
            yn = input("Did you mean %s instead? Enter Y if yes, or N for No.: " % get_close_matches(word, data.keys())[0])
            if yn == "Y":
                return data[get_close_matches(word, data.keys())[0]]

            elif yn == "N":
                return "The word doesnt exist. Please Try Again"

            else:
                return "We didn't understand anything"




    else:
        return "The word doesnt exist. Please Try Again"






word = input("Please input the word to search the meaning: ")

output = translate(word)

if type(output) ==list:
    for item in output:
        print(item)

else:
    print(output)
    # print(data["rain"])









