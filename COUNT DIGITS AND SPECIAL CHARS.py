s = "rah123@"
count = 0
sp = 0
for i in s:
    if i in "1234567890":
        count += 1
    if i in "!@#$%^&*()_+-":
        sp += 1
print("digits",count,"and special charecters",sp)
