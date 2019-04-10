
t = int(input())
pocket = []

def answer(t):
    for i in range(t):
        m = []
        total = 0

        for i in range(1, 11):
            n = [list(map(int, input().split()))]
            m.append(n)

        for j in range(len(m)):
            if m[j] % 2 != 0:
                total += m[j]
            else: continue

        pocket.append(total)

    for x in range(len(pocket)):
         print("#%d %d" % (x + 1, pocket[x]))

answer(t)