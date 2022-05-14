import operationEC
from fractions import Fraction

print("Curve Values y**2 = x**3 + ax + b ")
a = int(input("Enter Curve Values a "))
b = int(input("Enter Curve Values b "))
cur = (a, b)
p = int(input("Enter Prime Number : "))
print("Do you want Do \n\t1-Addition \n\t2-Multiplicative ")
c = int(input())

if (c==1) :
    p1X = int(input("Enter point 1 x value "))
    p1Y = int(input("Enter point 1 y value "))
    p1 = (p1X, p1Y)
    p2X = int(input("Enter point 2 x value "))
    p2Y = int(input("Enter point 2 y value "))
    p2 = (p2X, p2Y)
    print(operationEC.add(cur, p1, p2, p ))
elif(c==2):
    p1X = int(input("Enter point 1 x value "))
    p1Y = int(input("Enter point 1 y value "))
    p1 = (p1X, p1Y)
    n = int(input("Enter Scalar : "))
    print(operationEC.mutli(cur, p1 , n , p  ))

