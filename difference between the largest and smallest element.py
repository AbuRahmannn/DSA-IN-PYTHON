arr = [44, 6, 88, 33, 66, 2, 43, 9]

largest = arr[0]
smallest = arr[0]

for i in arr:
    if i > largest:
        largest = i

    if i < smallest:
        smallest = i

print(largest - smallest)