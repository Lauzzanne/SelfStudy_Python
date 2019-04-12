T = int(input())
test = [list(map(int, input().split())) for _ in range(T)]

for index, line in enumerate(test, 1):
    if line[0] > line[1]:
        result = ">"
    elif line[0] < line[1]:
        result = "<"
    else:
        result = "="
    print("#%d %s" % (index, result))