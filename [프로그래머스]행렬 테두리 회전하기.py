'''
[프로그래머스] 행렬 테두리 회전하기
'''

def solution(rows, columns, queries):
    answer = []
    matrix = [[j for j in range(i*columns+1, (i+1)*columns+1)] for i in range(rows)]
    
    for i in queries:
        turn = []
        k = matrix[i[2]-1][i[3]-1]
        
        for x in range(i[2]-i[0], 0, -1):
            turn.append(matrix[i[0]-1+x][i[3]-1])
            matrix[i[0]-1+x][i[3]-1]=matrix[i[0]-1+x-1][i[3]-1]

        for y in range(i[3]-i[1], 0, -1):
            turn.append(matrix[i[0]-1][i[1]+y-1])
            matrix[i[0]-1][i[1]+y-1]=matrix[i[0]-1][i[1]+y-1-1]

        for x in range(i[2]-i[0], 0, -1):
            turn.append(matrix[i[2]-x-1][i[1]-1])
            matrix[i[2]-x-1][i[1]-1]=matrix[i[2]-x+1-1][i[1]-1]

        for y in range(i[3]-i[1], 0, -1):
            turn.append(matrix[i[2]-1][i[3]-y-1])
            matrix[i[2]-1][i[3]-y-1]=matrix[i[2]-1][i[3]-y+1-1]

        matrix[i[2]-1][i[3]-2] = k
        answer.append(min(turn))
    return answer

print(solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]))
print(solution(3,3,[[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]))
