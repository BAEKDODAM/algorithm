'''
def solution(maps):
    answer = []
    days = 0
    def dfs(x,y):
        global days
        if x<=-1 or x>=len(maps) or y<=-1 or y>=len(maps[0]):
            return days
        if maps[x][y] != 'X':
            days += maps[x][y]
            maps[x][y] = 'X' # 방문처리

            dfs(x-1,y)
            dfs(x,y-1)
            dfs(x+1,y)
            dfs(x,y+1)
            #return days
    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if dfs(i,j) == 0:
                answer.append(-1)
            else: answer.append(days)
    return answer
'''

def solution(maps):
    answer = []

    for i in range(len(maps)):
        #maps[i] = maps[i].split('')
        maps[i] = list(maps[i])
    
    def dfs(x,y):
        #global total
        
        if x<=-1 or x>=len(maps) or y<=-1 or y>=len(maps[0]):
            return False
        
        if maps[x][y] != 'X':
            total = int(maps[x][y])
            maps[x][y] = 'X' # 방문처리
            total += dfs(x-1,y)+dfs(x,y-1)+dfs(x+1,y)+dfs(x,y+1)
            return total
        return False
        
    for i in range(len(maps)):
        for j in range(len(maps[i])):
            k =dfs(i,j)
            if k !=False :
                answer.append(k)

    return sorted(answer) if answer else [-1]


print(solution(["X591X","X1X5X","X231X", "1XXX1"]))
print(solution(["XX591X","XX1X5X","XX231X", "11XXX1"]))
'''
def solution(maps):
    answer = []
    for i in range(len(maps)):
        maps[i] = list(maps[i])
    
    def dfs(x,y):
        global total
        
        if x<=-1 or x>=len(maps) or y<=-1 or y>=len(maps[0]):
            return False
        
        if maps[x][y] != 'X':
            total = int(maps[x][y])
            maps[x][y] = 'X' # 방문처리
            total += dfs(x-1,y)+dfs(x,y-1)+dfs(x+1,y)+dfs(x,y+1)
            return total
        return False
        
    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if dfs(i,j)!=False :
                answer.append(total)
    if len(answer) == 0:
        answer.append(-1)
    return sorted(answer)
'''
