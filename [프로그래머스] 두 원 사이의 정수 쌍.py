'''
x축과 y축으로 이루어진 2차원 직교 좌표계에 중심이 원점인 서로 다른 크기의 원이 두 개 주어짐
반지름을 나타내는 두 정수 r1, r2가 매개변수로 주어질 때, 
두 원 사이의 공간에 x좌표와 y좌표가 모두 정수인 점의 개수를 return
※ 각 원 위의 점도 포함
1 ≤ r1 < r2 ≤ 1,000,000

풀이)
큰 원 내부 점 - 작은 원 내부 점 + 원 위의 점

'''
# 시간초과 나는 풀이
def solution(r1, r2):
    answer = 0
    m = 0
    for i in range(r2-1, r1-1,-1):
        for j in range(i,0,-1):
            d = (i**2+j**2)**(1/2)
            if r1> d:
                break
            elif r2 >= d:
                answer+=1
                if i==j:
                    m+=1
    answer = answer*8
    answer += (r2-r1+1)*4
    answer -= (m*4)
    return answer

'''
1. 우선 1사분면만 값을 구하면 4배를 해주면 된다고 생각한 뒤 접근함
2. x축으로 1부터 하나씩 늘려가며 r1과 r2 높이 계산
3. 두 높이 사이에 찍히는 점 수 계산
    - r2 높이는 내림해주고 r1 높이는 올림해준다(둘 사이에 찍히는 점을 계산해야 하므로)
    - 작은 원은 (r1,0)에(=작은원의 높이가 0인 경우) 무조건 점이 찍히기 때문에 +1 해줌
'''
import math
def solution2(r1, r2):
    answer = 0  
    
    for i in range(1, r2+1):
        high_r1 = math.sqrt(r2**2 - i**2)
        high_r2 = 0 if i>r1 else math.sqrt(r1**2 - i**2)
        
        answer += math.floor(high_r1) - math.ceil(high_r2) + 1
          
    return answer*4    
print(solution(3,5))