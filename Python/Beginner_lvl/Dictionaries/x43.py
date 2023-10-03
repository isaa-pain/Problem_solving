#Description:
#1-Write a Python program that sorts (in ascending order) the lists contained as values in a dictionary.
#2-The dictionary contains key-value pairs that match strings to lists. You need to sort these lists.
#3-The lists have to be mutated (changed).

dict_a={
	"a": [4, 3, 2],
	"b": [5, 3, 7],
	"c": [1, 9, 10],
	"d": [3, 4, 1]}
dict_b={}
for k,v in dict_a.items():
	dict_b[k]=sorted(v)
print(dict_b)
