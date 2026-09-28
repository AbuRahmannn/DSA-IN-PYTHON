#understand the assignment score
ass = [20, 18, 22, 15, 24, 19, 21, 23, 10, 12, 14, 16]
ass.sort(reverse = True)
eight = ass[0:8]
avg = sum(eight) / 8

#calculate the final score
exam = 45
if exam >= 0 and exam <= 100:
    final = (0.75 * exam) + (0.25 * avg)
    print("your final marks", final)

#check eligiblity
if avg >= 10 and exam >= 30 and final >= 40:
    print("Successfully Completed")
else:
    print("Not eligible")