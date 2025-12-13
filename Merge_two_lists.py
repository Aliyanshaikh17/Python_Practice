'''
Merge two lists
'''

list1 = [1, 2, 3]
list2 = [4, 5, 6]

merged = list1 + list2
print(merged)


'''
I tried solving it using user input.
'''

list1 = input("Enter first list items: ").split()
list2 = input("Enter second list items: ").split()

merged = list1 + list2
print("Merged List:", merged)
