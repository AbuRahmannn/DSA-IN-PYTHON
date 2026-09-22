nums = {
    "x" : 5,
    "y" : 6,
    "z" : 7
}
values = list(nums.items())
for i in range(len(nums)):
    for j in range(i+1,len(values)):
        if values[i][1] > values[j][1]:
            values[i], values[j] = values[j], values[i]
result = {}
for key,val in values:
    result[key] = val
print(result)