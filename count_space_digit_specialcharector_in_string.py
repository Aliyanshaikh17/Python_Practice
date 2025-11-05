'''
Count spaces, digits, and special characters in a string.
'''


text = input("Enter the string: ")
space_count = 0
digit_count = 0
special_count = 0

for ch in text:
    if ch == ' ':
        space_count += 1
    elif '0' <= ch <= '9':
        digit_count += 1
    elif not (('A' <= ch <= 'Z') or ('a' <= ch <= 'z')):
        special_count += 1

print("Spaces:", space_count)
print("Digits:", digit_count)
print("Special Characters:", special_count)


    
