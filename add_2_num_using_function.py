'''
add 2 numbers using a function
'''

def add_numbers(a, b):
    return a + b

num1 = int(input("Enter first number:- "))
num2 = int(input("Enter second number:- "))

result = add_numbers(num1, num2)
print("Sum =", result)


'''
add two numbers with using return statment
'''

def add(num1, num2):
    return num1 + num2

num1 = int(input("Enter first number:- "))
num2 = int(input("Enter second number:- "))

result = add(num1, num2)
print(result)
