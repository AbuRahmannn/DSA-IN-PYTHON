x = "kdbHH9i9"

digit = 0
upper = 0
lower = 0

for i in x:

    if i.isdigit():
        digit += 1

    if i.islower():
        lower += 1

    if i.isupper():
        upper += 1

print("lower:", lower)
print("upper:", upper)
print("digit:", digit)