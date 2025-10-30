'''
Convert kilometers to miles and vice versa.

'''
miles = float(input("Enter the distance in miles:- "))
kilometers = float(input("Enter the distance in kilometer:- ")) 
Miles_to_km = kilometers * 0.621371
Km_to_miles = miles * 1.60934
print(f"{miles} miles = {Miles_to_km} = kilometers")
print(f"{kilometers} kilometers = {Km_to_miles} miles")
