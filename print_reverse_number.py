'''
print reverse number of user input
'''

num = int(input("Enter the number :- "))
rev_num = 0
while num > 0:
    digit = num % 10
    rev_num = rev_num * 10 + digit
    num = num // 10
print(f"reverse number is :- {rev_num}")

