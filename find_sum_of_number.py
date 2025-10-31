'''
Find the sum of all numbers from 1 to n.
'''

n = int(input("Enter the number :- "))
sum = 0
for i in range(1, n + 1):
    sum += i
print("Sum =", sum)

