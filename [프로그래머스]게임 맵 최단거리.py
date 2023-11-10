'''
[프로그래머스] 게임 맵 최단거리

자기 자신 위치 [i,j]
동 서 남 북 [i,j+1] / [i,j-1] / [i+1,j] / [i-1,j]
'''
def solution(maps):
    n = len(maps)
    m = len(maps[0])
    answer = -1
    load = 0
    def dfs(x,y):
        nonlocal answer, load
        #if x == n-1 and y == m-1:
        #    load += 1
        #    answer.append(load)
        if x <= -1 or y <= -1 or x >= n or y >= m:
            return False
        if maps[x][y] == 1:
            maps[x][y] = 0 # 방문
            load += 1
            if x==n-1 and y==m-1:
                answer = load
            dfs(x, y+1)
            dfs(x, y-1)
            dfs(x+1, y)
            dfs(x-1, y)
            #print(load)
    dfs(0,0)
    return answer
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))




# 너비 우선 탐색
from collections import deque

def solution(maps):
    if len(maps) == 1 and len(maps[0]) == 1:
        return 1
    row_len = len(maps)
    vec_len = len(maps[0])
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    # 맵 받기
    def bfs():
        queue = deque()
        queue.append((0, 0))
        
        while queue:
            row, vec = queue.popleft()
            if (row, vec) == (row_len - 1, vec_len - 1):
                return maps[row][vec]
            for (y, x) in zip(dy, dx):
                new_row = row + y
                new_vec = vec + x
                if new_row < 0 or new_row >= row_len or \
                    new_vec < 0 or new_vec >= vec_len or \
                    maps[new_row][new_vec] == 0 or \
                    (maps[new_row][new_vec] != 1 and 
                     maps[new_row][new_vec] <= maps[row][vec] + 1):
                    continue
                maps[new_row][new_vec] = maps[row][vec] + 1
                queue.append((new_row, new_vec))
        return -1

    return bfs()

def solution_bfs(maps):
    n, m = len(maps), len(maps[0])
    visited = [[-1 for _ in range(m)] for _ in range(n)]
    visiting = deque([(0, 0)])
    visited[0][0] = 1
    dx, dy = [-1, 1, 0, 0], [0, 0, 1, -1]
    while visiting:
        x, y = visiting.popleft()
        for i in range(4):
            xx, yy = x + dx[i], y + dy[i]
            if 0 <= xx < n and 0 <= yy < m and maps[xx][yy] == 1 and visited[xx][yy] == -1:
                visited[xx][yy] = visited[x][y] + 1
                visiting.append((xx, yy))
    return visited[n-1][m-1]

