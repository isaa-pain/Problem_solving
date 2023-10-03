# Description:
#1-Write a Python program that counts the frequency of each value in a dictionary.
#2-The program should create a new dictionary to map each value in the original dictionary to its frequency (how many times it occurs).
#3-If the dictionary is empty, print an empty dictionary.
from collections import defaultdict
dict_a={
	"a": 4,
	"b": 4,
	"c": 2,
	"d": 7,
	"e": 4,
	"f": 2,
	"g": 7,
	"h": 7
 }
dict_b=defaultdict(int)
if not dict_a :
    print("empty !")
else :
    for values in dict_a.values():
        dict_b[values]+=1
print(dict_b)