'''
[프로그래머스] 주차 요금 계산

문제)
입차 기록, 출차기록을 통해 주차 요금 계산

풀이)
dict 사용하여 차 번호별로 주차시간 구하고 요금 계산
'''

import math

def solution(fees, records):
    carNum = []
    answer = []
    for i in range(len(records)):
        records[i] = records[i].split()
        carNum.append(records[i][1])

    carNum = sorted(carNum)
    cars = dict.fromkeys(carNum)
   
    # 차 사전에 주차 시간 추가
    for i in records:
        recordsMin = int(i[0][:2])*60 + int(i[0][3:5])
        if cars[i[1]]== None:
            cars[i[1]]=[recordsMin]
        else: cars[i[1]].append(recordsMin)
    
    for i in cars:
         # 빠져나오지 않은 차
        if len(cars.get(i))%2 > 0:
            cars[i].append(1439)

        # 주차한 시간 계산
        parkingMin = 0
        for j in range(0,len(cars.get(i)),2):
            parkingMin += cars.get(i)[j+1]-cars.get(i)[j]

        # 요금 계산
        if parkingMin-fees[0] > 0:
            answer.append(fees[1] + math.ceil((parkingMin-fees[0])/fees[2])*fees[3])        
        else:
            answer.append(fees[1])
    return answer


print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))

