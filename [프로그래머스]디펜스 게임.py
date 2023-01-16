'''
[프로그래머스] 디펜스 게임

리스트를 사용하여 풀이하였을때 계속 시간초과가 발생함

-> enemy의 길이가 최대 백만이기 때문에 시간 복잡도 O(nlogn)안에 풀어야 하는 문제다.
최소힙을 사용하여 풀었음

'''
import heapq
def solution(n, k, enemy):
    heap = []
    sumE = 0
    for i in range(len(enemy)):
        sumE += enemy[i]
        heapq.heappush(heap, -enemy[i])

        if sumE > n: # 카드사용
            x = heapq.heappop(heap)
            sumE += x
            if k < 1:
                return i
            else: k-=1
        if sumE==n and i == len(enemy)-1:
            return i+1
    return len(enemy)

