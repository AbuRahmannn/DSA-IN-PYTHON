num = 876
total = 0

while num > 0:
    digit = num % 10 #first digit
    total += digit 
    num = num // 10 #increment to next digit

print(total)