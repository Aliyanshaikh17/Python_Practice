"""
Write a program to check whether a person is a child, teenager, adult, or senior citizen.

"""

age = int(input("Enter your age:- "))
if age <= 12:
    print("You are child")
elif age >= 13 and age <= 19:
    print("You are a teenager")
elif age >= 20 and age <= 59:
    print("You are adult")
elif age >= 60:
    print("You are senior citizen ")
else:
    print("Invalid age")


