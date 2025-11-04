'''
Remove all vowels from a given string.
'''

text = input("Enter the string: ")

vowels = "aeiouAEIOU"
result = ""

for ch in text:
    if ch not in vowels:
        result += ch

print(f"String without vowels: {result}")
