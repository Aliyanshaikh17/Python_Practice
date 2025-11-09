'''
Print all prime numbers between 1 and 100
Logic :- two factor only, one is 1 and another is number itself
'''

print("Prime numbers between 1 and 100:")
for n in range(2, 101):          
    if all(n % i != 0 for i in range(2, n)):   
        print(n , end = " ")
