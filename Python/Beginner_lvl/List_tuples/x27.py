# Description:
#1-Write a Python program that prints a list with the elements that listA and listB have in common.
#2-If they don't have any elements in common, print an empty list.
#3-The program should not assume that the lists have the same length.
#4-You may assume that each element will only appear once in each list

list_a=[4,5,6]
list_b=[1,2,4,5]

print(list(set(list_a)&set(list_b)))