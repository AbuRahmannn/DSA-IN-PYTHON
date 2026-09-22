nums = {
    "x" : 5,
    "y" : 6,
    "z" : 7
}
reverse = {}
for i in nums:
    reverse[nums[i]] = i
print(reverse)