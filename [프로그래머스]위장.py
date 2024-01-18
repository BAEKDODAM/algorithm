# https://ddamm.notion.site/_-51e14d76140149e09e8f7c97965035ad?pvs=4

from collections import Counter
def solution1(clothes):
    answer = 1
    dic_clothes = dict(clothes)
    cnt_clothes = Counter(dic_clothes.values())
      
    for i in cnt_clothes.values():
        answer *= (i+1)
    return answer-1

def solution2(clothes):
    answer = 1
    hash_map = {}
    for clothe, type in clothes:
        hash_map[type] = hash_map.get(type, 0)+1 # type을 가지는 값이 있는지 확인하고 있으면 값을 가져오고 없으면 내가 정해둥 값인 0이 출력됨
    print(hash_map)
    for type in hash_map:
        answer *= (hash_map[type]+1)
    return answer-1

from functools import reduce
def solution3(clothes):
    answer = 1
    counter = Counter(type for chothe, type in clothes)
    print(counter)
    answer = reduce(lambda acc, cur: acc*(cur+1), counter.values(), 1)
    return answer-1

print(solution3([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
