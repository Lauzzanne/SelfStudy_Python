for i in range(1, int(input()) + 1):
    data = input()
    year = data[0:4]
    month = int(data[4:6])
    day = int(data[6:])
    day31 = [1, 3, 5, 7, 8, 10, 12]
    day30 = [4, 6, 9, 11]

    trueResult = "#%d %s/%s/%s" % (i, year, data[4:6], data[6:])
    falseResult = "#%d -1" % (i)

    if month in day31:
        if 1 <= day <= 31:
            print(trueResult)
        else:
            print(falseResult)
    elif month in day30:
        if 1 <= day <= 30:
            print(trueResult)
        else:
            print(falseResult)
    elif month == 2:
        if 1 <= day <= 28:
            print(trueResult)
        else:
            print(falseResult)
    else:
        print(falseResult)