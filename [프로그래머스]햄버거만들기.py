'''
[프로그래머스]햄버거 만들기
'''

def solution(ingredient):
    stack = []
    answer = 0
    for i in ingredient:
        stack.append(i)
        if stack[-4:] == [1,2,3,1]:
            answer+=1
            for i in range(4):
                stack.pop()   
    return answer

print(sol([2, 1, 1, 2, 3, 1, 2, 3, 1]))
