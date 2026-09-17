arr = [44,6,88,33,66,2,43,9]
k = 3
for i in range(3):
    arr.insert(0,arr[-1])
    arr.pop()
print(arr)