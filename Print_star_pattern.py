'''
Print star pattern
'''

for i in range(1, 4):
    print("*" * i)

'''
Print star pattern using user input
'''

rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):
    print("*" * i)