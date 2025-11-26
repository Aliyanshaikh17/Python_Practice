'''
check the number is power of or not 
'''

num = int(input("Enter the number :- "))
if num > 0 and (num & (num - 1)) == 0:
    print("Power of 2")
else:
    print("Not Power of 2")