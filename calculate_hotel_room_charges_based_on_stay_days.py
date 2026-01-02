'''
Write a program to calculate hotel room charges based on stay days.

'''

days_stay = int(input("Enter the number of stay days:- "))
charge = float(input("Enter the room charge per day:- "))
total_room_charges = days_stay * charge

print("Total Room Charges:- ", total_room_charges)
