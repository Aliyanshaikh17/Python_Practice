'''
Write a program to check whether a given number is a single-digit or double-digit number
'''

num = int(input("Enter the number:- "))

if -9 <= num <= 9:
    print("Single-digit number")
elif (-99 <= num <= -10) or (10 <= num <= 99):
    print("Double-digit number")
else:
    print("Number has more than two digits")
