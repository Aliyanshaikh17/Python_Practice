'''
Write a program to calculate insurance premium based on age and salary.
'''

age = int(input("Enter your age:- "))
salary = float(input("Enter your salary:- "))

if age < 30:
    premium = salary * 0.05
    print("5% insurance premium applied")
elif 30 <= age < 50:
    premium = salary * 0.08
    print("8% insurance premium applied")
else:
    premium = salary * 0.12
    print("12% insurance premium applied")

print("Insurance premium amount:", premium)
