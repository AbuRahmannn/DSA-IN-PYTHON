str = "dfhrebfkto"
alpha = True
for i in str:
    if i >= "0" and i <= "9":
        alpha = False
        break
if alpha:
    print("only aplhabets")
else:
    print("not only alphabets")