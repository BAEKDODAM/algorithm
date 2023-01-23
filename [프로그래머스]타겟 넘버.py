'''
[프로그래머스] 타겟 넘버

풀이)
dfs 사용
'''
sol = 0
def solution(numbers, target):
    answer = dfs(numbers, target, 0, 0)
    return answer

def dfs(numbers, target, i, x) : # i = 현재 노드, x = numbers 합
    n = len(numbers)
    global sol
    
    if i == n : # 최대 깊이 도달 
        if x == target : # 합이 target과 같아지면
            sol+=1
    else :
        dfs(numbers, target, i+1, x+numbers[i])
        dfs(numbers, target, i+1, x-numbers[i])
        
    return sol
