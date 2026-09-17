arr = [10, 20, 30, 40, 50, 60, 70, 80, 90]

total = 0
count = 0

for i in range(len(arr)):
    if i % 3 == 0:
        total += arr[i]
        count += 1

average = total / count

print("Sum:", total)
print("Average:", average)