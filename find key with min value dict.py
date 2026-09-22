#Check whether a key exists in a dictionary.
nums = {
    "x" : 5,
    "y" : 6,
    "z" : 7
}
small = float("inf")
small_key = ""
for key in nums:
    if nums[key] < small:
        small = nums[key]
        small_key = key
print(small_key)