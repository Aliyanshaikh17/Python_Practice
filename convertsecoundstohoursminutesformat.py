'''
onvert seconds to hours, minutes, and seconds format
'''
seconds = int(input("Enter time in seconds: "))
hours = seconds // 3600
seconds %= 3600
minutes = seconds // 60
seconds %= 60
print(f"Time: {hours} hours, {minutes} minutes, {seconds} seconds")