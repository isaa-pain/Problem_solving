#Description:
#1-Write a Python program that prints the largest(sum) of the values in a dictionary.
#2-You may assume that all the values in the dictionary are either lists or tuples.

dict_a={
	"a": [1, 2, 3321],
	"b": [4, 0, -4],
	"c": [3, 532, 999],
	"d": [45, 12, 100]
}
max_sum_value=max(sum(v) for v in dict_a.values())
print(max_sum_value)