'''
Write a program to calculate salary after deduction based on conditions
'''

salary = float(input("Enter your salary:- "))
deduction = 0

if salary >= 30000:
    deduction = salary * 0.10
    print("10* deduction applied")
    final_salary = salary - deduction
    print("Deduction amount:", deduction)
    print("Salary after deduction:", final_salary)

elif 5000 >= salary >= 15000:
    deduction = salary * 0.05
    print("5* deduction applied")
    final_salary = salary - deduction
    print("Deduction amount:", deduction)
    print("Salary after deduction:", final_salary)
    
else:
    print("No deduction applied")
