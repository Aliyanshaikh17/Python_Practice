'''
Check eligibility for voting 
'''
Age = int(input("Enter your age: "))

if Age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")    



''' method 2 '''


'''
Check eligibility for voting
'''
age = int(input("Enter your age: "))

print("You are eligible to vote.") if age >= 18 else print("You are not eligible to vote.")
