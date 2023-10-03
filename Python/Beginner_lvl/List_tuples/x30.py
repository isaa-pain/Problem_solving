# Description:
#1-Write a Python program that creates and print a dictionary that maps each element in a list to its corresponding frequency (how many times it occurs in the list).
#2-The test should be case-sensitive. Therefore, "A" should not be considered the same element as "a".


list_a=['a','a','b','c','a','A','b']
dict_b={}
for i in list_a:
    if i not in dict_b :
        dict_b[i]=1
    else:
        dict_b[i]=dict_b[i]+1
print(dict_b)