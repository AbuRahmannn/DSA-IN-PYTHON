str = "programming"
checked = ""
freq = []
for i in str:
    if i not in checked:
        count = 0
        for j in str:
            if i == j:
                count += 1
        freq.append(count)
        checked += i
max = freq[0]
index = 0
for i in range(len(freq)):
    if freq[i] > max:
        max = freq[i]
        index = i
print("char", checked[index])        
print("max frequency", max)