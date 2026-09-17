#pair of sum to target
arr = [1,2,3,4,5,6,7,9]
target = 6
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i] + arr[j] == target:
            print(arr[i],arr[j])