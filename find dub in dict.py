nums = {
    "a": 10,
    "b": 20,
    "c": 10,
    "d": 30,
    "e": 20
}
result = {}
for key,val in nums.items():
    if val not in result.values():
        result[key] = val
print(result)