str = "r@hm@n"
special = 0
for i in str:
    if not i.isalnum():
        special += 1
print(special)