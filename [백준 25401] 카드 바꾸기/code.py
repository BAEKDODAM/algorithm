N = int(input())

arr = [0] + list(map(int, input().split()))

def check(s, diff):
    cnt = 0
    for i in range(1, N + 1):
        s += diff
        if arr[i] != s:
            cnt += 1
    return cnt

ans = 500
for i in range(1, N):
    for j in range(i + 1, N + 1):
        diff = (arr[j] - arr[i]) / (j - i)

        if diff - int(diff) != 0:
            continue

        ans = min(ans, check(arr[i] - diff * i, diff))
print(ans)