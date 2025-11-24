'''
Check temperature level 
'''

temp = float(input("Enter temperature: "))

if temp > 30:
    print("Hot")
if 20 <= temp <= 30:
    print("Warm")
if temp < 20:
    print("Cold")

