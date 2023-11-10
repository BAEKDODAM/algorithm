def solution(chicken):
    answer = 0
    cp = 0
    while chicken//10 >= 1:
        answer += chicken//10
        chicken = chicken//10 + chicken % 10
    return answer

print(solution(1999))
print(solution(100))
print(solution(1081))

'''
1999
199 + 9 = 208
20 +8 = 28
2 + 8 = 10
1
'''
