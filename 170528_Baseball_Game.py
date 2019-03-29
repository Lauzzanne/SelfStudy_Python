from random import randint

numbers = []

# 수 생성
while len(numbers) < 3:
    new_number = randint(0, 9)
    while new_number in numbers:
        new_number = randint(0, 9)
    numbers.append(new_number)

print("0과 9 사이의 서로 다른 세 숫자를 랜덤한 순서로 뽑았습니다.")

# 숫자 입력받기
strike = 0
tries = 0

while strike < 3:
    # 초기화
    strike = 0
    ball = 0
    guess = []
    n = 1
    print("세 수를 하나씩 차례대로 입력하세요.")
    while len(guess) < len(numbers):
        user = int(input("%d 번째 수를 입력하세요." % n))
        if user > 9 or user < 0:
            print("범위를 벗어나는 수입니다. 다시 입력해 주세요.")
        elif user in guess:
            print("중복되는 수 입니다. 다시 입력해 주세요.")
        else:
            guess.append(user)
            n = n + 1
    tries += 1

    # 볼카운트
    for j in range(3):
        if numbers[j] == guess[j]:
            strike += 1
        elif numbers[j] in guess:
            ball += 1

    print("%dS %dB" % (strike, ball))
print("축하합니다. %d번만에 세 숫자의 값과 위치를 모두 맞추셨습니다." % tries)