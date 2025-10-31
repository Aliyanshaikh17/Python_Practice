'''
Check if a character is a vowel, consonant, digit, or special symbol.
'''
character = input("Enter a character to check if it is vowel, consonant, digit, or special symbol: ")

if character.isalpha():
    if character.lower() in ['a', 'e', 'i', 'o', 'u']:
        print("Vowel")
    else:
        print("Consonant")
elif character.isdigit():
    print("Digit")
elif not character.isalnum():
    print("Special Symbol")
else:
    print("Unknown Character Type")
