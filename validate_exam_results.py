'''
Write a program to validate exam results with grace marks logic.
'''


marks = int(input("Enter obtained marks:- "))
pass_marks = int(input("Enter passing marks:- "))
grace = int(input("Enter grace marks:- "))

if marks >= pass_marks:
    print("Result: Pass")
elif marks + grace >= pass_marks:
    print("Result: Pass with Grace")
else:
    print("Result: Fail")
