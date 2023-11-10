def solution(babbling):
    answer = 0
    word = ["aya", "ye", "woo", "ma"]
    for i in babbling:
        for j in word:
            if i.find(j) != -1:
                i = i.replace(j,"*")
        i = i.replace("*","")
        if len(i) == 0: answer+=1
    return answer

print(solution(["aya", "yee", "u", "maa", "wyeoo"]))

'''
*Check*
문자열에서 특정 문자열 변경(삭제)하는 함수
- replace(없애고 싶은 문자열, 새로 넣을 문자열)
- strip(없애고 싶은 문자)

문자열에서 특정 문자열 찾는 함수
- 문자열.find(찾고싶은 문자열)
'''
