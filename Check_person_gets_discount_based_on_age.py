'''Check if a person gets a discount based on age'''


age = int(input("Enter age: "))

if age < 5:
    print("Discount: 100% (Free)")
elif age <= 18:
    print("Discount: 50%")
else:
    print("No discount")
