#Description:
#1-Write a Python program that generates and prints all the possible permutations of a list.
#2-A permutation is a possible arrangement of the elements of the list. For example, [2, 1, 3] is a permutation of [1, 2, 3].
#3-Print each permutation as a list on a separate line. You can print them as lists or tuples.
#4-Include the list itself as a permutation

import itertools
list_a=[1,2,3]

list_output=itertools.permutations(list_a)

for i in list_output:
    print(list(i))