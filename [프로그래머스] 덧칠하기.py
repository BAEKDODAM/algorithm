def solution(n,m,section):
    if m==1 :
        return len(section)
    answer = 1
    arr = []
    for i in section:
        arr.append(i)
        
        # 만약 arr이 롤러 길이를 넘어가거나 칠해야하는 벽 끝과 끝 사이 길이가 롤러 길이를 넘어가면
        # 배열을 초기화하고 롤러의 시작점을 바꿈(배열을 다시 채움)
        if len(arr) > m or arr[-1] - arr[0] >= m :
            arr = arr[-1:]
            answer+=1
    return answer

print(solution(8,4,[2,3,6]))
