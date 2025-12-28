'''
Write a program to identify the type of triangle (equilateral, isosceles, scalene).
'''

a = int(input("Enter side a :- "))
b = int(input("Enter side b :- "))
c = int(input("Enter side c :- "))
if a == b == c:
    print("equilateral")
elif a == b or b == c or a == c:
    print("isosceles")
elif a != b and b != c and a != c:
    print("Scalene Triangle")
