'''
Write a program to check whether a number is less than or equal to 50.
'''

try:
    num = int(input("Enter a number:- "))
    if num <= 50:
        print(f"{num} is less than or equal to 50.")
    else:
        print(f"{num} is greater than 50.")

except ValueError:
    print("Invalid input Please enter a valid number ")