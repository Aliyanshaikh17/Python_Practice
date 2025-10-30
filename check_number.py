'''
Check if a number is positive, negative, or zero.

'''
try:
   num = float(input("Enter the number:- "))
   if num > 0:
    print("Number is positive")
   elif num < 0:
    print("Number is negetive")
   elif num == 0:
    print("Number is 0")
   else:
    print("Number is invaild")
  
except ValueError as e:
  print("Invalid input! Please enter a valid number.")