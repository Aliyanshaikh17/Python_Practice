'''
Check if ATM withdrawal amount is valid or not
'''

amount = int(input("Enter amount: "))

if amount <= 0:
    print("Invalid amount!")
elif amount < 100:
    print("Minimum withdrawal is 100.")
elif amount % 100 != 0:
    print("Invalid! Enter amount in multiples of 100.")
else:
    print("Valid withdrawal")
