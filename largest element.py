arr = [33,22,66,11,77]
print(max(arr))
#or
large = arr[0]
for i in arr:
    if i > large:
        large = i
print(large)        