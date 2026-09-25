num = 587
rev = 0

while num > 0:
    digit = num % 10 #first digit
    rev = rev * 10 + digit #last digit
    num = num // 10 #increment to next digit

print(rev)