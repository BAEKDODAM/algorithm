
n,m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(map(list(int, input())))

def dfs(x, y):
    # 재귀 종료 조건
    if x<0 or x>=n or y<0 or y>=m:
        return False

    # 방문 여부 확인
    if graph[x][y] == 0:
        # 방문처리
        graph[x][y] = 1

        # 상하좌우 재귀적으로 호출
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)

        return True
    return False

# 모든 노드 방문
result = 0
for i in range(n):
    for j in range(m):
        if dfs(n, m) == True:
            result += 1

print(result)
