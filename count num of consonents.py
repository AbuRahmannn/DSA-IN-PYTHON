str = "rahman"
vowels = 0
for i in str:
    if i not in "aeiou":
        vowels += 1
print(vowels)