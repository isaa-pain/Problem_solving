#Description:
#1-Write a Python program that checks if all values in a dictionary are equal.
#2-If they are, print True. Else, print False.
#3-If the dictionary is empty, print "Empty".

dict_a={'a':4,'b':4,'c':4}
if not dict_a:
    print('empty')
else:
    # Converting dict values into a set to get ridoff duplicates ,then we measure its len
    print(True if len(set(dict_a.values()))==1 else False)