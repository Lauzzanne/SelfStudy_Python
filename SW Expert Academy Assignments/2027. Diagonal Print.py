plus = 0

for i in range(5):
    for j in range(5):
        if j == plus:
            print("#", end='')
        else:
            print("+", end='')
    plus += 1
    print(' ')