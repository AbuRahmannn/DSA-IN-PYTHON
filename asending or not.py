arr = [44, 6, 88, 33, 66, 2, 43, 9]
#if arr == arr.sort():
#print("is in asending order")
#else:
#print("not in asending order")
asc = True
for i in range(len(arr)):
    if arr[i] > arr[i + 1]:
        asc = False
        break
if asc:
    print("yes")
else:
    print("not")