l = [1,3,3,1,5,6]
s = l.copy()
fq = []
s = set(s)
s = list(s) #1,3,5,6
for i in s:
    count = 0   
    for j in l:
        if j == i:
            count += 1
    print(i,":repeated:",count,": times")