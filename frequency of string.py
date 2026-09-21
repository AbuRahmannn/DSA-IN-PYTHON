str = "programming"
checked = ""
for i in str:
    if i not in checked:
        count = 0
        for j in str:
            if i == j:
                count += 1
        print(i, ":", count)
        checked += i
        