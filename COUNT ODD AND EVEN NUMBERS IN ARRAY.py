l = [23,34,12,78,34]
odd,even= 0,0
for i in l:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print("even",even)        
print("odd",odd)