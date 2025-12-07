'''
Check if a number is divisible by both 6 and 13.
'''

num = int(input("Enter a number: "))

if num % 6 == 0 and num % 13 == 0:
    print("The number is divisible by both 6 and 13.")
else:
    print("The number is not divisible by both 6 and 13.")
    
