l = [0,3,2,0,0,231]
count = 0
for i in l:
    if 0 in l:
        count += 1 
        l.remove(0)
        l.append(0)
print("number of zeros ",count)
print(l)
