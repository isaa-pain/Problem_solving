#Description:
#1-Write a Python program that prints the smallest value in a dictionary.
#2-If the dictionary is empty, print None.
#3-You may assume that the values are numeric.
#-----------------------------------------------------------
#Using 'Min' function here !
#-----------------------------------------------------------
dict_a={'a':4,'b':3,'c':6}
if not dict_a:
    print('None')
else:
    print(min(dict_a.values()))