from random import randint

# 무작위로 정렬된 1 - 45 사이의 숫자 여섯개 뽑기
def generate_numbers():
    numbers = []
    while len(numbers) < 6:
        num = randint(1, 45)
        if num not in numbers:
            numbers.append(num)
        else:
            num = randint(1, 45)
    return sorted(numbers)

# 보너스까지 포함해 7개 숫자 뽑기
# 정렬된 6개의 당첨 번호와 1개의 보너스 번호 리스트를 리턴
# 예: [1, 7, 13, 23, 31, 41, 15]
def draw_winning_numbers():
    winning_numbers = generate_numbers()
    bonusNumber = randint(1, 45)
    if bonusNumber not in winning_numbers:
        winning_numbers.append(bonusNumber)
    else:
        bonusNumber = randint(1, 45)
    return winning_numbers

# 두 리스트에서 중복되는 숫자가 몇개인지 구하기
def count_matching_numbers(numbers, winning_numbers):
    matching_numbers = 0
    for num in numbers:
        if num in winning_numbers:
            matching_numbers += 1
    return matching_numbers

# 로또 등수 확인하기
def check(numbers, winning_numbers):
    count = 0 # 일치 여부 확인
    bonus_count = 0
    for num in numbers:
        if num in winning_numbers[:6]:
            count += 1
        if num == winning_numbers[6]:
            bonus_count += 1

    if count == 6:
        return 1000000000
    elif count == 5 and bonus_count == 1:
        return 50000000
    elif count == 5:
        return 1000000
    elif count == 4:
        return 50000
    elif count == 3:
        return 5000
    else:
        return 0