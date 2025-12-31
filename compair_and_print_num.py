'''
Write a program to compare two numbers and print the greater one.

'''

num1 = int(input("Enter first number:-"))
num2 = int(input("Enter second number :- "))

if num1 > num2:
    print("First number is greater than second number ")
elif num2 > num1:
    print("Second number is greater than first number ")
else:
    print("both numbers are equal")