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
result = []
for i in dict1:
    if i not in dict2:
         result.append(i)
print(result)