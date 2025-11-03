'''
Count the number of digits in a given number.
'''

num = input("Enter the numbers: ")
count = 0
for ch in num:
    if ch.isdigit():
        count += 1
print(f"Number of digits:- {count}")
