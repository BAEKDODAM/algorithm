'''
문제)
오름차순 수열 주어질 때 아래 조건을 만족하는 부분수열 시작 인덱스와 마지막 인덱스 return
- 임의의 두 인덱스의 원소와 그 사이의 원소를 모두 포함하는 부분 수열임
- 부분수열의 합=k
- 합이 k인 부분 수열이 여러 개인 경우 길이가 짧은 수열을 찾음
- 길이가 짧은 수열이 여러 개인 경우 앞쪽에 나오는 수열을 찾음

매개변수 
- 열을 나타내는 정수 배열 sequence
- 부분 수열의 합을 나타내는 정수 k

조건
    5 ≤ sequence의 길이 ≤ 1,000,000
    1 ≤ sequence의 원소 ≤ 1,000
    sequence는 비내림차순으로 정렬되어 있습니다.
    5 ≤ k ≤ 1,000,000,000
    k는 항상 sequence의 부분 수열로 만들 수 있는 값입니다.

풀이) 포인터
    부분수열의 시작과 끝을 나타내는 포인터 s와 e를 사용
    0. 변수 선언
        - 리턴할 결과를 담을 start와 end
        - 시작 포인터와 끝 포인터 s와 e
        - 부분 배열의 길이 partLength
        - 부분 배열의 합 partSum
    1. e가 배열의 길이를 넘어가지 않고 s<=e 일 동안 반복문 실행
    2. 부분 배열의 합 > k면, 시작 포인터를 한 칸 앞으로 당기고 partSum 수정
    3. 부분 배열의 합 < k면, 끝 포인터를 한 칸 뒤로 당기고 
       e < len(sequence)이면 partSum 수정(index out of range 방지)
    4. 부분배열의 함 = k면, 부분 배열 길이를 비교해 짧으면 start와 end 갱신
       시작 인덱스를 한 칸 앞으로 당기고 partSum 수정
    5. return [start, end]
'''

def solution(sequence, k):
    start = 0
    end = 0
    s = 0
    e = 0
    partLength = len(sequence) # 부분배열의 길이
    partSum = sequence[0] 
    while s<=e<len(sequence):
        if partSum > k: 
            partSum -= sequence[s]
            s+=1
        elif partSum < k: 
            e+=1
            if e < len(sequence) :
                partSum += sequence[e]
        else: 
            if partLength > e-s: 
                partLength = e-s
                start = s
                end = e
            partSum -= sequence[s]
            s+=1
    return [start, end]

print(solution([1,2,3,4,5],7)) # [2, 3]
print(solution([1, 1, 1, 2, 3, 4, 5], 5)) # [6, 6]
print(solution([2, 2, 2, 2, 2], 6)) # [0, 2]