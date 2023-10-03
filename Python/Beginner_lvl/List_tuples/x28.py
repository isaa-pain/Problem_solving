#Description:
#1-Write a Python program that prints the second largest value in a list.
#2-If the list is empty or only has one element, print None.

list_a=[1,2,3,4]
#removing duplicated & backing up the set
list_o=list(set(list_a))
if not list_a or len(list_a)==1:
    print("None")
else:
    list_o.remove(max(list_o))
    print(max(list_o))