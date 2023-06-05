```
[프로그래머스/python] 숫자 문자열과 영단어

풀이)

solution2
 1. dic 자료형을 사용하여 영단어와 숫자 문자를 연결
 2. 이를 사용해 replace 함수를 활용하여 숫자 문자열의 영단어를 숫자로 교체

solution3
 1. enumerate를 사용하여 for문을 돌려서 영단어와 영단어의 인덱스를 동시에 순회
 2. replace 함수를 사용하여 인덱스와 영단어를 교체
 
```

def solution(s):
    arr = ['zero','one', 'two','three','four','five','six','seven','eight','nine']
    answer = ""
    tmp = ""
    for i in s:
        if i.isnumeric():
            answer += i
        else:
            tmp += i
            if tmp in arr:
                answer += str(arr.index(tmp))
                tmp = ""
    return int(answer)

def solution2(s):
    dic = {'zero':'0','one':'1', 'two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}
    for key in dic:
        s = s.replace(key, dic[key])

    return int(s)

def solution3(s):
    arr = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for i,c in enumerate(arr):
        s = s.replace(c,str(i))
    return int(s)



print(solution2("one4seveneightone"))
