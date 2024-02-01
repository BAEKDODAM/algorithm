'''
    문제) 다음달에 누가 가장 선물을 많이 받을지 예측
    - 두 사람 사이에 더 많이 선물 준 사람이 다음달에 선물 받음
    - 선물 주고받은 기록이 없거나 같으면 선물지수가 더 큰 사람이 다음달에 선물 받음
        = 선물지수 = 준 선물 수-받은 선물 수
    - friends = 친구 이름 담은 배열 
    - gifts = 친구들이 주고받은 선물 기록 배열

    조건
    - 2 <= friends 길이 = 친구들 수 <=50
    - 1 <= gifts 길이 <= 10,000

'''
import numpy as np
def solution(friends, gifts):
    result = [0]*len(friends)
    gift_cnt = [0]*len(friends)
    friend_gift = [[0] * len(friends) for _ in range(len(friends))]
    for i in gifts:
        gift = i.split(" ")
        friend_gift[friends.index(gift[0])][friends.index(gift[1])]+=1
    
    for i in range(len(gift_cnt)):
        for j in range(len(gift_cnt)):
            gift_cnt[i] += friend_gift[i][j]
            gift_cnt[i] -= friend_gift[j][i]
    for i in range(len(friends)):
        for j in range(i):
            if friend_gift[i][j] > friend_gift[j][i]:
                result[i]+=1
                print(i,j, result)
            elif friend_gift[i][j] < friend_gift[j][i]:
                result[j]+=1
            else:
                if gift_cnt[i] > gift_cnt[j]:
                    result[i] += 1
                elif gift_cnt[i] < gift_cnt[j]:
                    result[j] += 1

    return max(result)

print(solution(["muzi", "ryan", "frodo", "neo"],["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]))