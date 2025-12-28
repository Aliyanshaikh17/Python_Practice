'''
Write a program to create a menu-driven calculator using conditional statements.

'''

num1 = int(input("Enter the first number:- "))
num2 = int(input("Enter thr second number :- "))
choice = int(input("Enter choice (between 1 - 4):- "))

if choice == 1:
    result = num1 + num2
    print("Adition of 2 number is :- ", result)
elif choice == 2:
    result = num1 - num2
    print("substaction of 2 number is :- ", result)
elif choice == 3:
    result = num1 * num2
    print("multiplication of 2 number is :- ", result)
elif choice == 4:
    result = num1 / num2
    print("division of 2 number is :- ", result)
else:
    print("invalid choice")
