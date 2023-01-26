
# 내 풀이
# 이유는 모르겠으나 테스트12에서 오류 발생..
def solution(s):
    answer = 0
    for i in range(len(s)):
        stack = []
        x=0
        for j in s:
            x += 1
            if j == "{" or j=="[" or j=="(":
                stack.append(j)
            else:
                if len(stack) == 0:
                    break
                elif (j=="}" and stack[-1]=="{") or (j==")" and stack[-1]=="(") or (j=="]" and stack[-1]=="["):
                    stack.pop()
                else: break
        s = s[1:]+s[0]
        if len(stack) == 0 and x == len(s):
            answer+=1
    return answer


print(solution("[]{}()"))
print(solution("([)]"))


# 다른 사람 풀이 --------------------

def solution(s):
    answer = 0
    for i in range(len(s)):
        stack = []
        s += s[0]
        s = s[1:]
        torf = True
        for j in s:
            if j == '{' or j=='(' or j=='[':
                stack.append(j)
            else:
                if stack == []: 
                    torf = False
                    break
                if stack[-1]=='{' and j=='}' or stack[-1]=='(' and j==')' or stack[-1]=='[' and j==']':
                        stack.pop()
                else:
                    torf = False
                    break
        if stack == [] and torf == True:
            answer += 1
    return answer
