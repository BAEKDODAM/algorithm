def solution(location):
    cnt = 0
    # (위아래, 좌우)
    move = [(-2, -1), (-2,1),(2,-1),(2,1),(-1,-2),(1,-2),(-1,2),(1,2)]
    up_down = ord(location[0])-96
    left_right = int(location[1])
    for i in move:
        y = up_down + i[0]
        x = left_right + i[1]
        if x >= 1 and x <= 8 and y >= 1 and y <= 8 :
            cnt+=1
    return cnt
            
l = input()
print(solution(l))


'''
알파벳 숫자로 바꾸기
- ord() 사용
- A의  아스키코드 = 65, a의 아스키코드 = 97
'''
