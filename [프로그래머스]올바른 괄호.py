def solution(s):
    answer = True
    stack = []
    for i in s:
        if i =='(':
            stack.append(0)
        elif i==')':
            if len(stack)==0:
                answer = False
            else:
                stack.pop()
    if len(stack) != 0:
        answer = False

    return answer
