'''
Write a Python program to print all numbers between 
two user-given numbers that are divisible by both 6 and 13
'''

start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

for i in range(start, end + 1):
    if i % 6 == 0 and i % 13 == 0:
        print(i)