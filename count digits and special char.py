str = "rah@89n"
digits = 0
special = 0 #special char
for i in str:
    if i.isdigit():
        digits += 1
    if not i.isalnum():
        special += 1
print("digits:",digits)
print("special:",special)