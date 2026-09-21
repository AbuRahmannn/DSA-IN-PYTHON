#merge 2 dicts
nums1 = {
    "x" : 5,
    "y" : 6,
    "z" : 7
}

nums2 = {
    "a" : 1,
    "b" : 2,
    "c" : 3
}

nums1.update(nums2)
print(nums1)