'''
Write a program to check whether three sides can form a valid triangle
'''

a = int(input("Enter the first side :- "))
b = int(input("Enter the second side :- "))
c = int(input("Enter the third side :- "))

if a + b > c and a + c > b and b + c > a:
    print(" this is valid tranangle")
else:
    print("this is invalid trangle")
