
'''
Write a program to check whether a given date is valid.
'''


day = int(input("Enter day:- "))
month = int(input("Enter month:- "))
year = int(input("Enter the year:- "))

if month < 1 or month > 12:
    print("Invalid Date")
elif month in {1, 3, 5, 7, 8, 10, 12}:
    if 1 <= day <= 31:
        print("Valid Date")
    else:
        print("InValid Date")
elif month in {4, 6, 9, 11}:
    if 1 < day < 30:
        print("Valid Date")
    else:
        print("InValid Date")
elif month == 2:
     if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        if 1 < day < 29:
         print("Valid Date")
        else:
         print("InValid Date")
     else:
        if 1 <= day <= 28:
            print("Valid Date")
        else:
            print("Invalid Date")
    
else:
    print("Invalid Date")
