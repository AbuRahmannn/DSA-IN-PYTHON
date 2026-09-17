arr = [1,2,0,3,4,0,5,6,0,7,9]
count = 0
for i in arr:
    if i == 0:
        count += 1
while 0 in arr:
        arr.remove(0)
for j in range(count):
    arr.append(0)
print(arr)