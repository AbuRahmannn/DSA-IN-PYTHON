str = "rahman"
no_vowel = ""
for i in str:
    if i not in "aeiou":
        no_vowel += i

print(no_vowel)