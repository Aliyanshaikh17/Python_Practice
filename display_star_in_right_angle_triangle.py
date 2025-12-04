'''
write python program to display * in right angle triangle using for loop.
'''

A = int(input("Enter number of rows: "))

for i in range(1, A + 1):
    for j in range(i):
        print("*", end=" ")
    print()
