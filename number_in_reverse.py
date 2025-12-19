'''
Display numbers in reverse order (n to 1).
'''

num = int(input("Enter the number :- "))
for i in range(num,0,-1):
    print(i)



# i try to solve this example using while loop


num = int(input("Enter the number: "))

while num >= 1:
    print(num)
    num -= 1
