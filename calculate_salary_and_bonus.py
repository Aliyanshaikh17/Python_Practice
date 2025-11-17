'''
 Calculate salary after adding bonus
'''

salary = float(input())
bonus = float(input())   # bonus percentage

final_salary = salary + (salary * bonus / 100)
print("Final Salary:", final_salary)
