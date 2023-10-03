#Description:
#1-Write a Python program that determines if three numbers (a, b, and c) are in increasing order, decreasing order, or none.
#2-If a > b > c, print "Decreasing Order".
#3-If a < b < c, print "Increasing Order".
#4-Else, print "None".

a,b,c=(4,5,7)

if a>b and b>c :
    print("Decreasing")
elif a<b and b<c:
    print("Increasing")
else:
    print('None')