'''
    문제)
    다트를 세 개 던져 점수 합계로 실력을 겨루는 게임
    점수 계산 로직
        1. 게임 기회는 총 3번, 각 기회마다 0-10점까지 있음
        2. 점수와 함께 S, D, T 영역이 존재하고 각 영역 당첨시 점수에서 1제곱, 2제곱, 3제곱으로 계산됨
        3. 옵션으로 스타상 아차상 존재. 
           스타상* = 바로 전에 얻은 점수와 현재 점수 각각 *2, 아차상# = 현재 점수 마이너스
        4. 스타상(*)은 첫 번째 기회에서도 나올 수 있다. 이 경우 첫 번째 스타상(*)의 점수만 2배가 된다. (예제 4번 참고)
        5. 스타상(*)의 효과는 다른 스타상(*)의 효과와 중첩될 수 있다. 이 경우 중첩된 스타상(*) 점수는 4배가 된다. (예제 4번 참고)
        6. 스타상(*)의 효과는 아차상(#)의 효과와 중첩될 수 있다. 이 경우 중첩된 아차상(#)의 점수는 -2배가 된다. (예제 5번 참고)
        7. Single(S), Double(D), Triple(T)은 점수마다 하나씩 존재한다.
        8. 스타상(*), 아차상(#)은 점수마다 둘 중 하나만 존재할 수 있으며, 존재하지 않을 수도 있다.
'''

def solution(dartResult):
    answer = 0
    num = [0,0,0,0]
    sdt = ['S','D','T']
    n = 0
    dartResult = dartResult.replace('10','k')
    for i in range(len(dartResult)):
        if dartResult[i].isnumeric():
            num[n] = dartResult[i]
            n+=1
        elif dartResult[i] == 'k':
            num[n] = 10
            n+=1
        elif dartResult[i] in sdt:
            num[n-1] = int(num[n-1]) ** (sdt.index(dartResult[i])+1)
        elif dartResult[i] == '*':
            num[n-1] = num[n-1]*2
            if n>1:
                num[n-2] = num[n-2]*2
        elif dartResult[i] == '#':
            num[n-1] *= (-1)
    answer = num[0]+num[1]+num[2]
    return answer
print(solution(	"1D2S#10S"))
