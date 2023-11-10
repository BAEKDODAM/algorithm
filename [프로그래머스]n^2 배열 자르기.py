import numpy as np

# 시간초과 발생한 풀이
def solution(n, left, right):
    answer = []
    arr = np.zeros((n,n))
    [[0 for j in range(n)] for i in range(n)]
    
    
    for i in range(n):
        for j in range(i+1):
            arr[i][j] = i+1
            arr[j][i] = i+1
    print(arr)
    
    for m in range(n):
        answer.extend(arr[m])
        
    print(answer)
    
    return answer[left:right+1]


def solution2(n, left, right):
    answer = []
    for i in range(rignt-left+1):
        (left + i + 1) // n
        if (left + i + 1) % n == 1 :
            answer[i] = (left + i + 1) // n + 1
        elif (left + i + 1) % n == 2 :
            answer[i] = (left + i + 1) // n
        
    
    arr = [[i+1 for j in range(n)] for i in range(n)]
    print(arr)
    return arr

print(solution2(4, 7, 14))
