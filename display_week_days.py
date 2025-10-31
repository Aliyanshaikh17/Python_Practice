'''
Display the day name based on user input (1 for Monday, 2 for Tuesday...).

'''


Day = int(input(" Please enter the week days (1 to 7):-"))
if Day == 1:
    print("Monday")
elif Day == 2:
    print("Tuesday")
elif Day == 3:
    print("Wednesday")
elif Day == 4:
    print("Thursday")
elif Day == 5:
    print("Friday")
elif Day == 6:
    print("Saturday")
elif Day == 7:
    print("Sunday")
else:
    print("Invalid week day! Please enter a number from 1 to 7.")




