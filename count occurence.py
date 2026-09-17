#Count the occurrences of a given element.
arr = [22,66,22,66,44]
target = 66
count = 0
for i in arr:
    if i == target:
        count += 1
print(count)