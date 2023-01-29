'''
[프로그래머스] 카펫
- 완전탐색

'''


def solution(brown, yellow):
    i = 1
    while i <= yellow/i:
        if yellow%i == 0:
            if brown == ((i+1)+(yellow/i)+1)*2:
                break
        i += 1
    return [int(yellow/i+2), i+2]

print(solution(24,24))
