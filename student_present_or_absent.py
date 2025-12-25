'''
Write a program to check whether a student is present or absent based on input.
'''

status = input("Enter status (present/absent): ")
if status == "present":
    print("Student is present")
elif status == "absend":
    print("Student is absent")
else:
    print("invalid input")
    