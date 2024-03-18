N, K = map(int, input().split())

def solution(N, K):
    ball = N - K*(K+1)/2

    if ball < 0:
        return -1
    if ball%K !=0: return K
    return K-1

print(solution(N, K))