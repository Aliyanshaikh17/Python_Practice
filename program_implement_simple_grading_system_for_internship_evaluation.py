'''
Write a program to implement a simple grading system for an internship evaluation.
'''

marks = int(input("Enter internship evaluation marks:- "))

if marks >= 90:
    print("Grade A - Excellent")
elif marks >= 75:
    print("Grade B - Very Good")
elif marks >= 60:
    print("Grade C - Good")
elif marks >= 50:
    print("Grade D - Average")
else:
    print("Fail")
