nums = {
    "a": 10,
    "b": 20,
    "c": 10,
    "d": 30,
    "e": 20
}
dub = []
values = set(nums.values())
print(values)
result = {}
for key,val in values:
    result[key] = val
print(result)