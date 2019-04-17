T = int(input())
test = [list(map(int, input().split())) for _ in range(T)]

for index, line in enumerate(test, 1):
    for num in line:
        quotient = int(line[0] / line[1])
        remainder = line[0] % line[1]
    print("#%d" % index, quotient, remainder)