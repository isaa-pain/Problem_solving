#Description:
#1-Write a Python program that prints the largest value in a dictionary.
#2-If the dictionary is empty, print None.
#3-You may assume that the values are numeric.

dict_a={'a':4,'b':33,'c':9}
max_a=0
corresponding_key=''
if not dict_a:
    print('None')
else:

    for k,v in dict_a.items():
        if v>max_a:
            max_a=v
            corresponding_key=k
print(corresponding_key,'->',max_a)