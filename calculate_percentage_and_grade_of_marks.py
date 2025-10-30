'''
Calculate percentage and grade from marks of 5 subjects
'''


marks = (92,75,40,14,93)
Total = sum(marks)
percentage = (Total / 500) * 100
if percentage >= 90:
    grade = "A"
elif percentage >= 80:
    grade = "b"
elif percentage >= 70:
    grade = "c"
elif percentage >= 60:
    grade = "d"
elif percentage >= 50:
    grade = "e"
else:
    print("You are fail in exam")

print("----- Result -----")
print(f"Total Marks: {Total}/500")
print(f"Percentage: {percentage:.2f}%")
print(f"Grade:- {grade}")