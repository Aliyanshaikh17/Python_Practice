'''
Write a program to simulate an online exam result system.
'''

marks = int(input("Enter obtained marks:- "))
pass_marks = int(input("Enter passing marks:- "))

if marks >= pass_marks:
    print("Result = You are Pass in exam")
else:
    print("Result = You are Fail in exam")
