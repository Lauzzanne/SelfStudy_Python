for i in range(1, int(input()) + 1):
    exercise = input().split()
    if int(exercise[2]) > int(exercise[1]):
        result = -1
    elif int(exercise[2]) < int(exercise[0]):
        result = int(exercise[0]) - int(exercise[2])
    else:
        result = 0

    print("#%d %d" % (i, result))