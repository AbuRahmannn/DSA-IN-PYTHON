str1 = "triangle"
str2 = "integral"
count = 0
if len(str1) == len(str2):
    for i in str1:
        for j in str2:
            if i == j:
                count =+1 
            if count == len(str1):
                break
    print("anagram")
else:
    print("not anagram")
