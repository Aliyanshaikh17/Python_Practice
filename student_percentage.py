'''
calculate a percentage and grade of student ( 5 subject )
'''

# Calculate Percentage and Grade for 5 subjects

sub1 = float(input("Enter marks of Subject 1: "))
sub2 = float(input("Enter marks of Subject 2: "))
sub3 = float(input("Enter marks of Subject 3: "))
sub4 = float(input("Enter marks of Subject 4: "))
sub5 = float(input("Enter marks of Subject 5: "))

total_marks_obtained = sub1 + sub2 + sub3 + sub4 + sub5
total_max_marks = 5 * 100  
percentage = (total_marks_obtained / total_max_marks) * 100

print(f"\nTotal Marks Obtained: {total_marks_obtained}")
print(f"Percentage: {percentage:.2f}%")


if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B+"
elif percentage >= 60:
    grade = "B"
elif percentage >= 50:
    grade = "C"
elif percentage >= 40:
    grade = "D"
else:
    grade = "Fail"

print(f"Grade: {grade}")

    