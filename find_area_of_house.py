'''
find the area of house
'''

''' without using functions '''

hight = float(input("Enter the hight of house :- "))
length = float(input("Enter the length of house :- "))
Area = hight * length

print(f"Area of house is :- {Area}")




print("----------------------------------------------------------")



''' with using functions '''

def house_area(height, length):
    return height * length

h = float(input("Enter the height of house: "))
l = float(input("Enter the length of house: "))

print(f"Area of house is: {house_area(h, l)}")
