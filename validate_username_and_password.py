'''
Write a program to validate username and password
'''

username = input("Enter your username:- ")
password = input("Enter your password:- ")
stored_username = "aliyan12"
stored_password = "7499"

if username == stored_username and password == stored_password:
    print("valid login")
else:
    print("invalid username or password")
