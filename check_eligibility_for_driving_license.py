'''
Check if a person is eligible for a driving license (age ≥ 18).
'''

age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible for a driving license.")
else:
    print("You are not eligible for a driving license.")


''' i try to solve this example another way 
Using (One-line if-else)
'''

age = int(input("Enter your age: "))

print("You are eligible for a driving license." if age >= 18 else "You are not eligible for a driving license.")
