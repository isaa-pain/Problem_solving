#Description:
#1-Write a Python program that creates and displays a dictionary that maps each letter in a string to how many times the character occurs in the string (its frequency).
#2-The dictionary should only include the characters in the string.
#3-The test should be case-insensitive ("A" should be counted as "a").
#4-The keys in the dictionary should be lowercase letters.
#5-Only include letters in the dictionary.
import string
from collections import defaultdict
string_a="Hello, World"
dict_b=defaultdict(int)
for c in string_a.lower():
    if c.isalpha():
        dict_b[c]+=1
print(dict_b)