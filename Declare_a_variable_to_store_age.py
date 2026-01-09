'''
Declare a variable to store your age and print it
'''

age = 22
print(age)


#with user input

age = int(input("Enter your age:- "))
print(age)


# Checking age category
if age < 18:
    print("You are a minor.")
elif age < 60:
    print("You are an adult.")
else:
    print("You are a senior citizen.")