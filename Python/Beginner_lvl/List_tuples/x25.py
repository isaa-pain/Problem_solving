# Description:
# 1-Write a Python program that prints (as a list) the elements of listA that are not in listB as a list.
# 2-If the lists have the same elements, print an empty list.
# 3-If listA is an empty list, print an empty list.

a=[1,2,3,4]
b=[3,4]
if not a :
    print('-- a is empty --')
else:
    print(list(set(a)-set(b)))

