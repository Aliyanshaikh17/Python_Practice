'''
Write a program to simulate an ATM withdrawal system with balance validation.

'''

withdraw_amount = float(input("Enter withdraw amount:- "))
balance = 10000
if withdraw_amount <= balance and withdraw_amount > 0:
    balance = balance - withdraw_amount
    print("Withdrawal successful")
    print("New balance:", balance)
else:
    print("invalid amount or Insufficient balance ")
