'''
    문제)
    N명의 학생의 이름과 국어, 영어, 수학 점수가 주어짐
    1. 국어 점수 내림차순으로 정렬
    2. 영어 점수 오름차순으로 정렬
    3. 수학 점수 내림차순으로 정렬 
    4. 이름 사전 순 정렬
    위 순서대로 정렬하여 학생 이름 출력
    
    조건)
    - 1 ≤ N ≤ 100,000
    - 1초

    풀이)
    N이 최대 10만이므로 시간복잡도 O(nlogn) 넘으면 안됨
    lambda 사용하여 sort()하기
    시간 복잡도를 낮추기 위해 sys.stdin.readline() 사용
'''
import sys 
N = int(sys.stdin.readline())

arr = []
for _ in range(N):
    name, *scores = sys.stdin.readline().split()
    arr.append((name, *map(int, scores)))

arr.sort(key=lambda x : (-x[1], x[2], -x[3], x[0]))

for st in arr:
    print(st[0])