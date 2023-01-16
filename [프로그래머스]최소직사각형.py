'''
[프로그래머스] 최소 직사각형
heapq을 사용하여 풀이하였다

아래 solution2는 가장 짧은 풀이다
'''
import heapq
def solution(size):
    heapW = []
    heapH = []
    for i in range(len(size)):
        heapq.heappush(heapW, -max(size[i]))
        heapq.heappush(heapH, -min(size[i]))
    answer = heapq.heappop(heapW) * heapq.heappop(heapH)
    return answer
print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))


def solution2(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)

    
