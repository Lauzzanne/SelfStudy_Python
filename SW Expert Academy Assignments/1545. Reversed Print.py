number = int(input())
i = 0

while number >= i:
    print(number - i, end = " ")
    i += 1

# or
for i in range(number, -1, -1):
    print(i, end = " ")