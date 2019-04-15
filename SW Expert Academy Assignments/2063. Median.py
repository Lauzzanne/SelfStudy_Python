T = int(input())
pocket = input().split()

for i in range(len(pocket)):
    pocket[i] = int(pocket[i])

center = int(len(pocket) / 2)

pocket.sort()
print(pocket[center])