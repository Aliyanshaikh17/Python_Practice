'''
Check loan eligibility (age + income)
'''

age = int(input("Enter age: "))
income = int(input("Enter monthly income: "))

if age >= 21 and income >= 20000:
    print("Eligible for loan")
else:
    print("Not eligible")