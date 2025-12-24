'''
Write a program to implement a simple traffic light system
'''

signal = input("Enter traffic signal (red / yellow / green): ")
if signal == "red":
    print("stop")
elif signal == "yellow":
    print("Get Ready")
elif signal == "green":
    print("Go")
else:
    print("Invalid Signal")
