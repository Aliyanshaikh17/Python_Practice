'''
Write a program to calculate bonus based on years of service
'''

salary = float(input("Enter the salary:- "))
years = int(input("Enter years of service:- "))

bonus = 0

if years >= 10:
    bonus = salary * 0.20
    print("I apply total 20 percent bonus")
    print(f"Your total bonus is :- {bonus}")

    final_salary = salary + bonus
    print("Final salary:", final_salary)

elif 5 <= years < 10:
    bonus = salary * 0.10
    print("I apply total 10 percent bonus")
    print(f"Your total bonus is :- {bonus}")

    final_salary = salary + bonus
    print("Final salary:", final_salary)


else:
    print("No bonus")
