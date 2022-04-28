def dfs(C, F, s, t):
        stack = [s]
        paths={s:[]}
        if s == t:
                return paths[s]
        while(stack):
                u = stack.pop(0)
                for v in range(len(C)):
                        if(C[u][v]-F[u][v]>0) and v not in paths:
                                paths[v] = paths[u]+[(u,v)]
                                if v == t:
                                        return paths[v]
                                stack.append(v)
        return None

def max_flow(C, s, t):
        n = len(C) # C is the capacity matrix
        F = [[0] * n for i in range(n)]
        path = dfs(C, F, s, t)
        print(path)
        while path != None:
            flow = min(C[u][v] - F[u][v] for u,v in path)
            for u,v in path:
                F[u][v] += flow
                F[v][u] -= flow
            path = dfs(C,F,s,t)
            print(path)
        return sum(F[s][i] for i in range(n))
    
# make a capacity graph
# node s  o  p  q  r  t
C = [[0, 3, 4, 5, 0, 0, 0, 0],
    [0, 0, 0, 0, 3, 1, 0, 0],
    [0, 0, 0, 0, 2, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 7, 0],
    [0, 0, 0, 0, 0, 0, 0, 5],
    [0, 0, 0, 0, 0, 0, 0, 3],
    [0, 0, 0, 0, 1, 0, 0, 4],
    [0, 0, 0, 0, 0, 0, 0, 0]]  

source = 0  
sink = 7   
max_flow_value = max_flow(C, source, sink)
print(max_flow_value)
