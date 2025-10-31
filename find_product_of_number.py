'''
Find the product of all numbers from 1 to n.
'''

n = int(input("Enter the value of n :- "))
product = 1
for i in range(1, n+1):
    product = product * i
print(product)
