'''
Write a program to check whether a number is a multiple of 10.

'''

num = int(input("Enter the number:- "))
if num % 10 == 0:
    print(f"{num} is a multiple of 10")
else:
    print(f"{num} is not a multiple of 10")
