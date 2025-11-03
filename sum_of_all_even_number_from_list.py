'''
Find the sum of all even number from list
'''

list = [15, 31, 32, 44, 76, 88]
sum_even = 0
for num in list:
    if num % 2 == 0:
        sum_even = sum_even + num
print(f"sum of even number from list is :-{sum_even}")

