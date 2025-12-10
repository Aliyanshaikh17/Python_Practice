'''
Swap two numbers 
'''

num1 = int(input("Enter first number:- "))
num2 = int(input("Enter second number:- "))
num1, num2 = num2, num1

print("After swapping:")
print("first number is:-", num1)
print("second number is :- ", num2)




'''
i try to solve this example in another way
'''

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

temp = num1
num1 = num2
num2 = temp

print("After swapping:")
print("First number:", num1)
print("Second number:", num2)

