l = [1,2,3,4,5]
k  = -1
n = len(l)
k = k % n # 2 % 5 = 2
print(l[k:] + l[:k])