nums = {
    "x" : 5,
    "y" : 6,
    "z" : 7
}
keys  = list(nums.keys())
for i in range(len(nums)):
    for j in range(i+1,len(keys)):
        if keys[i] > keys[j]:
            keys[i], keys[j] = keys[j], keys[i]
result = {}
for key in keys:
    result[key] = nums[key]
print(result)