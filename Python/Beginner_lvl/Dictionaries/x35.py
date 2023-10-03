#Description:
#1-Write a Python program that merges two dictionaries and prints the resulting dictionary.
#2-"Merging" the dictionaries involves making a new dictionary with the key-value pairs in both dictionaries

dict_a = {"a": 1, "b": 2, "c": 3}
dict_b = {"c": 4, "d": 6, "e": 8}

#The output should be:
#final_dict = {'a': 1, 'b': 2, 'c': 4, 'd': 6, 'e': 8}

final_dict={**dict_a,**dict_b}
print(final_dict)