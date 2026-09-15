l = [2,-2,3,-3,4,-4,0]
l1 = []
for i in l:
    if i < 0:
        l1.append(i)
        l.remove(i)
print(l1+l)