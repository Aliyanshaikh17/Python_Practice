'''
Write a program to calculate electricity bill based on units consumed
'''

units = float(input("total electricity units consumed:- "))

r1 = float(input("rate per unit for first slab (0-100 units):- "))

r2 = float(input("rate per unit for second slab (101-200 units):- "))

r3 = float(input("rate per unit for third slab (above 200 units) "))

bill = bill = (units <= 100) * (units * r1) + \
       (units > 100 and units <= 200) * ((100 * r1) + (units - 100) * r2) + \
       (units > 200) * ((100 * r1) + (100 * r2) + (units - 200) * r3)


print(f"Your electricity bill is :- {bill}")
