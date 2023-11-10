import math
def solution2(num, total):
    answer = []
    n = total // num
    m = total % num
    if m !=0 :
        answer = list(range(n-num//2+1, n+num//2+1))
    else:
        answer = list(range(n-num//2, n+num//2+1))
    return answer

def solution(num, total):
    m = 0
    if total % num>0: m=1
    return list(range(total//num - num//2 + m, total//num + num//2 + 1))

print(solution(3, 12))
print(solution(5,15))
print(solution(4,14))
print(solution(5,5))
