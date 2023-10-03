#Description:
#1-Write a Python program that creates a dictionary from the values contained in nested lists.
#2-Each nested list has this format [value1, value2].
#3-value1 should be the key in the dictionary and value2 should be its corresponding value.
#4-If there are no nested lists, print an empty dictionary.

list_a=[["a", 1], ["b", 2], ["c", 3], ["d", 4]]
list_b={}
if not list_a:
    print("empty !")
else:
    list_b=dict(list_a)
print(list_b)