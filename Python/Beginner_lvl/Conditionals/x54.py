#Description:
#1-Write a Python program that prints if a given year was (or will) be a leap year.
#Tip: A leap year is "a year, occurring once every four years, that has 366 days including February 29 as an intercalary day." (Definition by Oxford Languages).
#This is how you can determine if a year is a leap year or not:
#if (year is not divisible by 4) then (it is a common year).
#else if (year is not divisible by 100) then (it is a leap year)
#else if (year is not divisible by 400) then (it is a common year)
#else (it is a leap year)

year=int(input("Type in a year: "))
if not(year%4==0) :
    print("{year} is a common year!".format(year=year))
elif not(year%100==0):
    print("{year} is a leap year!".format(year=year))
elif not(year%400==0):
    print("{year} is a common year!".format(year=year))
else:
    print("{year} is a leap year!".format(year=year))