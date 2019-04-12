T = int(input())
test = [list(map(int, input().split())) for _ in range(T)]

for idx, line in enumerate(test, 1):
    max = line[0]
    for num in line:
        if num > max:
            max = num
    print('#%d' % idx, max)