l = [1,2,3,4,5]
k  = input("enter Kth value")
n = len(l)
k = k % n # 2 % 5 = 2
print(l[k:] + l[:k])