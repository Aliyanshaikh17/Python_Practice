'''
Write a program to simulate a railway ticket fare system based on age.
'''

age = int(input("Enter your age:- "))
base_fare = float(input("Enter base fare:- "))

if age < 5:
    fare = 0
    print("Ticket is free")
elif 5 <= age < 12:
    fare = base_fare * 0.50
    print("50% fare applied")
elif 12 <= age < 60:
    fare = base_fare
    print("Full fare applied")
else:
    fare = base_fare * 0.60
    print("Senior citizen discount applied")

print("Final ticket fare: is:- ", fare)
