'''
Check if a number is divisible by both 5 and 11.
'''

num = int(input("Enter a number: "))

if num % 5 == 0 and num % 11 == 0:
    print("The number is divisible by both 5 and 11.")
else:
    print("The number is not divisible by both 5 and 11.")