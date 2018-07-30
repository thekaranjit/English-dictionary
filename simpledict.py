# Simple Program using PyDictionary
from PyDictionary import PyDictionary

user_input = input("Please input a word to check the meaning: ")

dictionary=PyDictionary()


res = dictionary.meaning(user_input)

print(res)