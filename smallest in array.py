arr = [33,44,12,14,48]
print(min(arr))
#or
small = arr[0]
for i in arr:
    if i < small:
        small = i
print(small)