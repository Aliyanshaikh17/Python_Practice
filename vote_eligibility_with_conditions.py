'''
vote eligibility with conditions

condition 1 :- if age is greater then equal to 21 allow to vote .
condition 2 :- if age is lass than 21 not allow to vote .
condition 3 :- if age is greater then 65 is not allow to vote .
'''


'''
with using if and elif statments
'''
Age = int(input("Enter your age :- "))

if Age >= 21:
    print("you are eligible for vote")
elif Age < 21:
    print ("you are not eligible for vote ")
elif Age > 65:
    print ("you are not eligible for vote ")




'''
with using if and else statments
'''
Age = int(input("Enter your age :- "))
# if Age >= 21 and Age <= 64:
#     print("you are eligible for vote")
if 21 <= Age < 65:
    print("Eligible for voting")
else:
    print("you are not eligible for vote")
