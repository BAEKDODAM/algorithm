'''
문제
    전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인
    전화번호부에 적힌 전화번호를 담은 배열이 매개변수로 주어짐 = phone_book
    어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true를 return

제한 사항
    - 1 ≤ phone_book ≤ 1,000,000
    - 1≤ 각 전화번호의 길이 ≤ 20
    - 같은 전화번호가 중복해서 들어있지않음
'''

# 시간초과 발생
def solution1(phoneBook):    
    # 1. 비교할 A선택
    for i in range(len(phoneBook)):
        # 2. 비교할 B선택
        for j in range(i+1, len(phoneBook)):
            # 3. 서로가 서로의 접두어인지 확인한다.
            if phoneBook[i].startswith(phoneBook[j]):
                return False
            if phoneBook[j].startswith(phoneBook[i]):
                return False
    return True


def solution2(phoneBook):
    # 1. 전화번호를 soriting 한다
    phoneBook.sort()

    # 2. 전화번호를 2개씩 확인하여 접두어인지 확인한다
    for i in range(len(phoneBook)-1):
        if phoneBook[i+1].startswith(phoneBook[i]):
            return False
    return True

# zip을 사용한 solution2
def solution2_2(phoneBook):
    phoneBook.sort()
    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        print(p1, p2)
        if p2.startswith(p1):
            return False
    return True

def solution3(phoneBook):
    # 1. hash map을 만든다
    hash_map = {}
    for number in phoneBook:
        hash_map[number] = 1

    # 2. 접두어가 hash map에 존재하는지 찾는다
    for phone_number in phoneBook:
        start = ''  # 접두어
        for number in phone_number:
            start += number

            # 3. 접두어를 찾는다(기존 번호와 같은 경우는 제외)
            if start in hash_map and start != phone_number:
                return False
    return True

print(solution3(["12","634","6"]))