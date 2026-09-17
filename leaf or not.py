year = 2025
if year % 400 == 0 or year % 4 == 0 or year % 100 != 0:
    print("is a not leap year")
else:
    print("not a leaf year")