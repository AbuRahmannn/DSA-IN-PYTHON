dict1 = {
    "x" : 5,
    "y" : 6,
    "z" : 7
}    
dict2 = {
    "a" : 1,
    "b" : 5,
    "c" :3
}
common = []
for i in dict1.values():
    if i in dict2.values():
        common.append(i)
print(common)