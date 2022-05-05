def DFS(C, F, s, t): # (용량, 유량, 시작점, 도착점)
    stack = [s] # 시작점을 stack에 담음
    paths={s:[]}

    if s == t: # 시작점과 도착점이 같아지면 경로 반환
        return paths[s]
    
    while(stack): 
        u = stack.pop() # 맨 마지막 요소 호출 후 삭제(섭입후출)

        for v in range(len(C)): # 노드 개수 만큼 반복
            
            # 남은 용량이 0 이상이고 v가 경로에 포함되지 않으면 paths에 추가
            if(C[u][v]-F[u][v] > 0) and v not in paths:
                paths[v] = paths[u]+[(u,v)]

                # 목적지 t에 도달하면 paths 반환
                if v == t: 
                    return paths[v]

                stack.append(v)
    return None

def BFS(C, parent, s, t): 
    visited = [False]*len(C)
    queue = [] # BFS를 위한 큐 생성

    # 소스 노드는 방문한 것으로 표시하고 큐에 삽입
    queue.append(s)
    visited[s]=True

    while queue:
        u = queue.pop(0) # 선입선출, 큐에서 가장 앞 원소 꺼내 u에 담고 삭제

        # 디큐된 u의 인접한 모든 정점을 가져온다.
        # 방문하지 않은 정점인 경우 방문했음을 표시하고 큐에 넣는다.
        for v in range(len(C)): 
            if visited[v] == False and C[u][v] > 0:
                queue.append(v)
                visited[v] = True # 방문처리
                parent[v] = u # 내가 거쳐온 길(바로 이전 길)
                
                if v == t: # 목적지(sink)에 도달하면 true를 리턴(BFS 종료)
                    return True

    # source부터 시작해서 BFS에 있는 sink에 도달하지 못하면 false를 반환
    return False
           
    
def FordFulkerson(C, s, t):
    n = len(C) 
    F = [[0] * n for i in range(n)]

    path = DFS(C, F, s, t)
    while path != None:
        flow = min(C[u][v] - F[u][v] for u,v in path) # 경로의 용량들 중 최소 용량을 유량에 담는다

        # 유량 상쇄
        for u,v in path:
            F[u][v] += flow
            F[v][u] -= flow
        path = DFS(C,F,s,t)

    return sum(F[s][i] for i in range(n))

def EdmondsKarp(C, source, sink):
    parent = [-1]*len(C) # 이 배열은 BFS 및 저장 경로로 채워진다.
    max_flow = 0 # 초기 유량은 0

     # source에서 sink까지 경로가 있는 동안 flow 증가
    while BFS(C, parent, source, sink):
        
        path_flow = float("inf") # 양의 무한대 값
        s = sink

        # 도착지(sink)에 도달하지 않은 경우
        # BFS가 채운 경로를 따라 용량들 중 작은 값이 path_flow가 됨
        while(s != source): 
            path_flow = min(path_flow, C[parent[s]][s])
            s = parent[s]

        max_flow += path_flow # 전체 flow에 경로 flow 추가

        # 유량상쇄, 잔존 용량 업데이트
        v = sink
        while(v != source):
            u = parent[v]
            C[u][v] -= path_flow
            C[v][u] += path_flow
            v = parent[v]
    return max_flow


C = [[0, 16, 13, 0, 0, 0],
     [0, 0, 10, 12, 0, 0],
     [0, 4, 0, 0, 14, 0],
     [0, 0, 9, 0, 0, 20],
     [0, 0, 0, 7, 0, 4],
     [0, 0, 0, 0, 0, 0] ]

source = 0
sink = 5    

print("Ford-Fulkerson algorithm")
print("The maximum possible flow is", FordFulkerson(C, source, sink))
print("Edmonds-Karp algorithm")
print("The maximum possible flow is", EdmondsKarp(C, source, sink))
