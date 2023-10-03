#Description:
#"""Write a Python program that prints the positive and negative solutions (roots)
#for a quadratic equation.
#If the equation only has one solution, print the solution as the output.
#If it has two solutions, print the negative one first and the positive one second
#on the same line.
#If the equation has no real solutions, print "Complex Roots".
#You can determine the number of solutions with the discriminant
# (the result of b^2 - 4ac in the formula below).
#- If it's negative, the equation has no real solutions (only complex roots).
#- If it's 0, there is only one solution.
#- If it's positive, there are two real solutions."""#
#Considering a,b,c as coef for  (ax^2+bx+c)
from __future__ import division
from math import sqrt
re1,im1,re2,im2=0,0,0,0
a,b,c=(3,4,5)
sol1,sol2=0,0
discriminant= b*b - 4*a*c
if discriminant>0:
    sol1=((b*-1)-sqrt(discriminant))/(2*a)
    sol2=((b*-1)+sqrt(discriminant))/(2*a)
    print("Solutions to {a}x^2+{b}x+{c}: ".format(a=a, b=b, c=c))
    print("First Solution: {sol1} ".format(sol1=sol1))
    print("Second Solution: {sol2} ".format(sol2=sol2))
elif discriminant==0:
    sol1=(b*-1)/(2*a)
    print("Solutions to {a}x^2+{b}x+{c}: ".format(a=a, b=b, c=c))
    print("Only Solution: {sol1}".format(sol1=sol1))

else:

        #'Saving imaginary numbers in a list [Re,Im]'
     re1=(b*-1)/(2*a)
     im1=(-1*sqrt(-1*discriminant))/(2*a)
     re2=(b*-1)/(2*a)
     im2=sqrt(-1*discriminant)/(2*a)
     sol1=[re1,im1]
     sol2=[re2,im2]
     print("Solutions to {a}x^2+{b}x+{c}: ".format(a=a, b=b, c=c))
     print("First Solution: {sol1R} - i({sol1I})".format(sol1R=sol1[0],sol1I=sol1[1]))
     print("Second Solution: {sol2R} + i({sol2I})".format(sol2R=sol2[0],sol2I=sol2[1]))

