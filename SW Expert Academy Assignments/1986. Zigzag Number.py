for i in range(1, int(input()) + 1):
    numbers = int(input())
    total = 0
    for j in range(1, numbers + 1):
        if j % 2 == 0:
            j = -j
        total += j

    print("#%d %d" % (i, total))