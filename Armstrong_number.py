'''
Write a program to check whether a number is an Armstrong number.
'''

num = int(input("Enter the number:- "))
temp = num
n = len(str(num))
armstrong_sum = 0

while temp > 0:
    digit = temp % 10
    armstrong_sum += digit ** n
    temp //= 10
if armstrong_sum == num:
    print("The number is an Armstrong number")
else:
    print("The number is not an Armstrong number")
