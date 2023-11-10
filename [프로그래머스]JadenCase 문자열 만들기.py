def solution(s):
    s = list(s)
    for i in range(len(s)):
        if i == 0 and type(s[i]) == str:
                s[i] = s[i].upper()
        elif type(s[i]) == str and s[i-1] == ' ':
            s[i] = s[i].upper()
        else:
            s[i] = s[i].lower()
    return ''.join(i for i in s)

print(solution("3people unFollowed me"))


# 다른 사람 풀이 ----------
# title() 문자열 내 띄어쓰기 기준으로 각 단어의 첫글자는 대문자로, 나머지는 소문자로 변환한다.

def Jaden_Case(s):
    return s.title()
