#Find Maximum Numbers of Array
arr5 = [101,1,13,8,100,20,30]
max = arr5[0]
for i in arr5:
    if i > max:
      max = i
print(f"The maximum element is:", {max})