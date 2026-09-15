s = "RaHmaN"
u,l = 0,0
for i in s:
    if i in s.lower():
        l += 1
    else:
        u += 1
print("upper",u,"and lower",l)        
