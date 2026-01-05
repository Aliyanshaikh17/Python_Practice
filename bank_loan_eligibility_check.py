'''
Write a program to implement a bank loan eligibility system.
'''

age = int(input("Enter yout age:- "))
salary = float(input("Enter your annual salary:- "))
credit_score = int(input("Enter credit score:- "))

if age >= 21 and salary >= 25000 and credit_score >= 650:
    print("You are eligible for a bank loan")
else:
    print("You are not eligible for a bank loan")