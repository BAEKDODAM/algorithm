'''
[프로그래머스/python] 롤케이크 자르기
롤케이크를 두 조가그로 잘라 나눠먹음
토핑 공평하게 (조각 크기. 토핑 개수 상관x)

돌아가며 자르고
중복제거했을 때 배열 길이 같으면 공평
공평하면 answer+1

'''

from collections import Counter
def solution1(topping):
    answer = 0
    m = [0 for i in range(len(set(topping)))]
    y = [0 for i in range(len(set(topping)))]
    print(m,y)
    for i in topping:
        y[i-1]+=1
    print('초기', m, y)
    for i in topping:
        y[i-1] = y[i-1]-1
        m[i-1] = m[i-1]+1
        print('0 개수', m.count(0), y.count(0))
        if m.count(0) == y.count(0):
            answer+=1
            print('동등',m,y)
        elif m.count(0) < y.count(0):
            return answer
        
def solution(topping):
    answer = 0
    m=[]
    y=[]
    print(m,y)
    for i in topping:
        y[i-1]+=1
    print('초기', m, y)
    for i in topping:
        y[i-1] = y[i-1]-1
        m[i-1] = m[i-1]+1
        print('0 개수', m.count(0), y.count(0))
        if m.count(0) == y.count(0):
            answer+=1
            print('동등',m,y)
        elif m.count(0) < y.count(0):
            return answer
print(Counter([1,1,1,2,2,3,3,3,4]))

print(solution1([1, 2, 1, 3, 1, 4, 1, 2]))
print(solution([2,1,1,1,1,1]))
