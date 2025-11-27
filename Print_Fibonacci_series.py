'''
Print Fibonacci series up to n terms.

'''

num = int(input("Enter the number of terms: "))
a = 0
b = 1
print("Fibonacci Series:")
for i in range(num):
    print(a, end=" ")
    a, b = b, a + b
