'''
[프로그래머스]부족한 금액 계산하기
'''
def solution(price, money, count):
    answer = 0
    for i in range(1,count+1):
        answer += price*i
    if money-answer > -1:
        return 0
    else: return (answer-money)
    
def solution(price, money, count):
    pay = (((count+1)*count)/2) * price - price
    return max(0,pay)


