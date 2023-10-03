#Description:
#1-Write a Python program that simulates an interactive calculator with the basic arithmetic operations in Python (addition, subtraction, multiplication, division, integer division, and modulo).
#2-The program must interact with the user by asking for the values and the type of operation that will be performed.
#3-The output should include the values, the operation, and the result .

from __future__ import division
print("-----------------------------------------------------")
print("Calculator, Your operations must follow This Syntax")
print("value_a {Operation} value_b")
print("--------------------------------------------------------")
value_a=int(input("value_a :"))
operation=input("Operation: ")
value_b=int(input("value_b :"))
match operation:
    case '+':print("{value_a} {operation} {value_b} =".format(value_a=value_a,value_b=value_b,operation=operation),value_a+value_b)
    case '-':print("{value_a} {operation} {value_b} =".format(value_a=value_a,value_b=value_b,operation=operation),value_a-value_b)
    case '*':print("{value_a} {operation} {value_b} =".format(value_a=value_a,value_b=value_b,operation=operation),value_a*value_b)
    case '/':
        try:
            print("{value_a} {operation} {value_b} =".format(value_a=value_a,value_b=value_b,operation=operation),value_a/value_b)
        except ZeroDivisionError:
            print("Invalid devision")
    case r'//':
        try:
            print("{value_a} {operation} {value_b} =".format(value_a=value_a,value_b=value_b,operation=operation),value_a//value_b)
        except ZeroDivisionError:
            print("Invalid devision")
    case _:  print("{value_a} {operation} {value_b} =".format(value_a=value_a,value_b=value_b,operation=operation),value_a%value_b)

