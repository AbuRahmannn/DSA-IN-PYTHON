#count no of even and odd numbers
arr = [23,87,43,22,88,44,87]
odd, even = 0,0
for i in arr:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print("even: ", even, "odd: ", odd)