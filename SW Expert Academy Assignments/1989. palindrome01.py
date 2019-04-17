for i in range(1, int(input()) + 1):
    words = input()
    value = len(words) // 2
    for j in range(0, value):
        if words[j] == words[len(words) - j - 1]:
            result = 1
        else:
            result = 0
    print("#%d %d" % (i, result))