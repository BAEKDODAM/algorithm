# [백준 11659] 구간 합 구하기 4 (python)

## 문제

[백준 11659. 구간 합 구하기 4](https://www.acmicpc.net/problem/11659)

수 N개가 주어졌을 때, i번째 수부터 j번째 수까지 합을 구하는 프로그램을 작성하시오.

### 입력

- 첫째 줄: 수의 개수 N과 합을 구해야 하는 횟수 M
- 둘째 줄: N개의 수
    
    수는 1,000보다 작거나 같은 자연수이다. 
    
- 셋째 줄~ M개의 줄: 합을 구해야 하는 구간 i와 j

### 제한

- 1 ≤ N ≤ 100,000
- 1 ≤ M ≤ 100,000
- 1 ≤ i ≤ j ≤ N

### 입출력 예제

```
5 3
5 4 3 2 1
1 3
2 4
5 5
```

```
12
9
1
```

## 풀이

1. 입력받기
    
    ```python
    import sys
    input = sys.stdin.readline
    
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    ```
    
2. 합배열 생성
    1. 합배열 sum[n]의 값 = 입력받은 숫자 배열의 인덱스 0~n 까지의 합
    
    ```python
    sum = [0]
    sum.append(nums[0])
    for k in range(2,N+1):
        sum.append(sum[k-1]+nums[k-1])
    ```
    
3. 원하는 범위 시작값의 합배열과 끝값의 합배열 서로 빼주고 출력
    
    ```python
    for _ in range(M):
        i, j = map(int, input().split())
        print(sum[j]-sum[i-1])
    ```
    

### 전체 코드

```python
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))

sum = [0]
sum.append(nums[0])
for k in range(2,N+1):
    sum.append(sum[k-1]+nums[k-1])
    
for _ in range(M):
    i, j = map(int, input().split())
    print(sum[j]-sum[i-1])

```