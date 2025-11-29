'''
Reverse a string without using built-in reverse().
'''


str = input("Enter a string:- ")
rev = ""

for ch in str:
    rev = ch + rev

print("Reversed string:", rev)
