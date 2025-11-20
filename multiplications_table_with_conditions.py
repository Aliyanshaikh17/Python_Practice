'''
multiplications table with conditions
condition 1 :- user enter a number and output will be table
condition 2 :- and also print additions from zero to till that number

'''
number = int(input("Enter the number :- "))
for i in range(1,11):
        print(f"{number} * {i} = {number * i}")


total = 0
for i in range(number + 1):
    total = total + i
print(f"sum of {number} is :- {total}")
