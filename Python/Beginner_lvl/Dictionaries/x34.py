#Description:
#1-Write a Python program that adds a new key-value pair to a dictionary only if the key doesn't exist already.
#2-If the key-value pair exists in the dictionary, do not update the existing value. The dictionary should not be modified in this case.
#3-Store the new key in the new_key variable and the new value in the new_value variable.
#4-Print the final value of the dictionary.

dict_a={'January':1}
new_key='April'
new_value=9
if new_key not in dict_a:
    dict_a[new_key]=new_value
else:
    print('The key already exists in the dictionary')
print(dict_a)