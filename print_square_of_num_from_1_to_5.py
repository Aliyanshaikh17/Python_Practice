'''
Write a program to print the square of numbers from 1 to 5 using a for loop
'''

for i in range(1, 6):
    print(i * i)


#using user input

n = int(input("Enter the last number: "))

for i in range(1, n + 1):
    print(i * i)
