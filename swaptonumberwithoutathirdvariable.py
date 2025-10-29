#Swap two numbers without using a third variable.
m1 = int(input("Enter marks of first student :- "))
m2 = int(input("Enter marks of second student :- "))
m1,m2 = m2,m1
print(m1)
print(m2)