'''
Write a program to implement an online shopping discount system.
'''


total_amount = float(input("Enter the amount:- "))
discount = 0

if total_amount > 10000:
    discount = total_amount * 0.30
    print("I apply total 30 percent discount")
    print(f" Your total discount is :- {discount}")

    final_amount = total_amount - discount
    print("Final amount ",final_amount)

elif 1000 < total_amount < 5000: 
    discount = total_amount * 0.20
    print("I apply total 20 percent discount")

    print(f" Your total discount is :- {discount}")
    final_amount = total_amount - discount
    print("Final amount ",final_amount)

else:
    print("no discount")

