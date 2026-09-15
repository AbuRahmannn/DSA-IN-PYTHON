n = int(input())
for _ in range(n):
    sh, sm, eh, em = map(int,input().split())
    if em < sm:
        em = em + 60
        eh = eh - 1
    minutes = em - sm
    hours = eh - sh
    print(hours, minutes)
