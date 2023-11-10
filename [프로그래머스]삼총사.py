'''
세명 저수 더했을 때 0이 되면 삼총사
삼총사가 될 수 있는 방법이 몇개인지 return

3명씩 뽑는 경우의 수 모두 계산하여 0이 되는 것 count
'''
from itertools import combinations

def solution(number):
    count = 0
    for i in combinations(number, 3):
        if i[0]+i[1]+i[2] == 0:
            count+=1
    return count

print(solution([-2,3,0,2,-5]))
