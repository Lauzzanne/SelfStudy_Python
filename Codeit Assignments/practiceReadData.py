in_file = open('chicken.txt', 'r')

day = 0
total = 0 # 한달 매출

for line in in_file:
    data = line.strip().split(": ")
    amount = int(data[1])
    total += amount
    day += 1

in_file.close()

print(total / day)
