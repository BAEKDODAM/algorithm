'''
[프로그래머스] 푸드 파이트 대회
'''

def solution(food):
    foodList = []
    answer = ''
    for i in range(1,len(food)):
        for j in range(int(food[i])//2):
            foodList.insert(len(foodList)//2,i)
            foodList.insert(len(foodList)//2+1,i)
    for i in foodList:
        answer += str(i)
    return answer
print(solution([1, 3, 4, 6]))



# 다른 사람 풀이 -------------------

def solution(food):
    answer ="0"
    for i in range(len(food)-1, 0,-1):
        c = int(food[i]/2)
        while c>0:
            answer = str(i) + answer + str(i)
            c -= 1
    return answer
