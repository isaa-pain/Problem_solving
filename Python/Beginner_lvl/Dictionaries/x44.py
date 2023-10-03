#Description:
#1-Write a Python program that takes the content of a dictionary and converts it into a list of lists.
#2-Each nested list should contain a key as the first element and its corresponding value as the second element.
#3-Print the final list of lists.

dict_a= {
	"description": "shoe",
	"price": 4.56,
	"colors": ["green", "blue", "red"],
}
list_b=[list(v) for v in dict_a.items()]
print(list_b)
