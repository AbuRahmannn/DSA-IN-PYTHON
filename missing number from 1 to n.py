arr = [1,2,3,4,5,6,7,9]
n = 9
total = n*(n+1)//2
for i in arr:
    total -= i
print(total)