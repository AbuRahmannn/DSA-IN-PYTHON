dict1 = {
    "x" : 5,
    "y" : 6,
    "z" : 7
}    
dict2 = {
    "a" : 1,
    "x" : 2,
    "c" :3
}
common = []
for i in dict1.keys():
        if i in dict2.keys():
            common.append(i)
print(common)