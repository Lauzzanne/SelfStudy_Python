T = int(input())
i = 1

while i <= T:
    if T % i == 0:
        print(i, end=' ')
    i += 1