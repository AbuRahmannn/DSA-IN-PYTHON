str = "rahman"
freq = {}
for i in str:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
min = float("inf")
char = ""
for i in freq:
    if freq[i] < min:
        min = freq[i]
        char = i
print("char",char)
print("min frequency",min)