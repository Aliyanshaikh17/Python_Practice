'''
Write a python program to convert the temperature 
Fahrenheit to Celsius and vice versa.
'''
F = float(input("Enter the temperature in Fahrenheit :- "))
C = (F - 32)*5/9
print(f"{F} Fahrenheit -> {C} Celsius")

Celsius = float(input("Enter temperature in Celsius :- "))
F = (Celsius * 9/5)+32
print(f"{Celsius} Celsius -> {F} Fahrenheit.")
