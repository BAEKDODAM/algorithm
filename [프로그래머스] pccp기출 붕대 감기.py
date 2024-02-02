'''
    문제) 붕대감기는 1초동안 x만큼 체력 회복함
    t초 연속 붕대 감기를 설공하면 y만큼의 추가 체력 회복됨
    기술을 쓰는 도중 공격을 당하면 기술이 취소됨 -> 다시 붕대 감기를 하면 연속 성공 시간이 0으로 초기화됨
    공격 당하는 순간에는 체력 회복 불가
    현재 체력이 0 이하가 되면 끝    
    모든 공격이 끝난 직후 남은 체력을 return 
    
    - bandage = [붕대감기 기술 시전 시간, 1초당 회복량, 추가 회복량]
    - health = 최대 체력
    - attacks = [몬스터 공격 시간, 피해량]

'''
def solution(bandage, health, attacks):
    # 연속 성공 기록용 변수
    healthSuccess = 0
    # 현재 체력
    presentHealth = health
    # for 공격 배열
    for i in range(len(attacks)):
        if i == 0:
            healthSuccess = attacks[i][0] - 1
        # 현재 공격받은 시간 - 이전에 공격받은 시간 -1 = 붕대감기 연속 성공 시간
        else: healthSuccess = attacks[i][0] - attacks[i-1][0] -1
        # 연속 성공한 만큼 체력 회복, 단 최대 체력넘어갈 수 없음
        presentHealth += healthSuccess*bandage[1] 
        # 만약 연속 성공 시간이 기술시전시간(bandage)보다 크거나 같으면 체력+추가회복량
        if healthSuccess >= bandage[0]:
            presentHealth += (healthSuccess//bandage[0])*bandage[2]
        # 체력이 최대 체력량을 넘어가면 안됨
        if presentHealth > health:
            presentHealth = health
        
        # 공격 만큼 체력 감소
        presentHealth -= attacks[i][1]
        if presentHealth <= 0: return-1
    return presentHealth
print(solution([1, 1, 1], 5, [[1, 2], [3, 2]]))
print(solution([5, 1, 5], 30, [[2, 10], [9, 15], [10, 5], [11, 5]]))
print(solution([4, 2, 7], 20, [[1, 15], [5, 16], [8, 6]]))
