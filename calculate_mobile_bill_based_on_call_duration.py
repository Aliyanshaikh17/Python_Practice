'''
Write a program to calculate mobile bill based on call duration
'''

minutes = int(input("Enter total call duration (in minutes):- "))
bill = 0

if minutes <= 100:
    bill = minutes * 1
elif minutes <= 200:
    bill = (100 * 1) + ((minutes - 100) * 2)
else:
    bill = (100 * 1) + (100 * 2) + ((minutes - 200) * 3)

print("Total Call Duration:- ", minutes, "minutes")
print("Total Mobile Bill:- ₹", bill)
