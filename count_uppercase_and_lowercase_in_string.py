'''
Count uppercase and lowercase letters in a string.
'''

letter = input("Enter the string:- ")
uppercase = 0
lowercase = 0
for char in letter:
    if 'A' <= char <= 'Z':
        uppercase += 1
    elif 'a' <= char <= 'z':
        lowercase += 1

print(f"Uppercase letters: {uppercase}")
print(f"Lowercase letters: {lowercase}")

