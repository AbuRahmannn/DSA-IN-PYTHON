str = "3342342t3"
digit = True
for i in str:
    if i < "0" or i > "9":
        digit = False
if digit:
    print("only digits")
else:
    print("not only digits")