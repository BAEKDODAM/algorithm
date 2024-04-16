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
