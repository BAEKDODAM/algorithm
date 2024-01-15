'''
문제) [프로그래머스] 완주하지 못한 선수
    마라톤에 참여한 선수들의 이름이 담긴 배열 participant
    완주한 선수 이름이 담긴 배열 completion
    완주하지 못한 선수 이름 출력
    1<= 참여한 선수 수 <= 100,000
    completion의 길이는 participant의 길이보다 1 작습니다.

풀이)
    1. sorting/loop을 활용
    2. hash를 활용
    3. collectionsCounter 활용
'''

def solution1(participant, completion):
    # 두 리스트룰 sorting(정렬)
    participant.sort()
    completion.sort()
    # completion list의 length만큼 돌면서 completion에만 존재하는 한 명 찾기
    for i  in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    # list를 모두 순회해도 답이 없다면 마지막 주자가 완주하지 못한 선수이다.
    
    return participant[len(participant)-1]

def solution2(participant, completion):
    hashDict = {}
    sumHash = 0
    # hash를 key로 갖고 participant의 이름을 value로 갖는 dictionary를 만들고 합을 구한다
    for part in participant:
        hashDict[hash(part)] = part
        sumHash += hash(part)
    # 합에서 completion의 hash들의 합을 뺀다
    for comp in completion:
        sumHash -= hash(comp)
    # 마지막에 남은 hash가 완주하지 못한 선수의 hash다
    return hashDict[sumHash]

from collections import Counter
def solution3(participant, completion):
    # participant와 completion의 Counter를 구한다
    part_counter = Counter(participant)
    comp_counter = Counter(completion)
    # 둘의 차를 구하면 객체 1개 짜리 Counter를 반환한다
    answer = part_counter-comp_counter # answer의 타입을 Counter이기 때문에 list로 형변환해준 뒤 출력
    # Counter의  Key값을 return한다
    return list(answer.keys())[0]