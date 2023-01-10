'''
[프로그래머스] 과일 장수

풀이
1. sorted를 사용하여 과일 등급이 높은 순으로 정렬
2. 정렬한 과일 중 마지막 m번째에 담기는 과일이 최하 등급 과일임
3. 최하 등급 과일 *m 하여 과일 상자 가격 을 answer에 담음
4. 과일을 모두 상자에 담을 때까지 반복

'''
def solution(k, m, score):
    answer = 0
    apple_sort = sorted(score, reverse = True)
    for i in range(len(score)):       
        if (i+1)%m == 0:
            answer += apple_sort[i]*m
    return answer

print(solution(3, 4, [1,2,3,1,2,3,1]))
print(solution(4, 3, [4,1,2,2,4,4,4,4,1,2,4,2]))
