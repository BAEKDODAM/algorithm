import math
def solution2(storey):
    l = len(str(storey))
    #num = storey
    answer = 0
    #for i in range(l):
    while storey > 0:
        #n = num // math.pow(10, l-i-1)
        #num %= math.pow(10, l-i-1)
        #print("n= ",n )

        num = storey % 10

        if num < 5:
            answer += num;
            
        elif num > 5 :
            answer = answer + 10 + num
            storey += 10

        else:
            if (storey // 10) % 10 > 4:
                storey += 10
            answer += num
        storey //= 10
            

    return answer;
def solution(storey):
    answer = 0

    while storey:
        remainder = storey % 10
        # 6 ~ 9
        if remainder > 5:
            answer += (10 - remainder)
            storey += 10
        # 0 ~ 4
        elif remainder < 5:
            answer += remainder
        # 5
        else:
            if (storey // 10) % 10 > 4:
                storey += 10
            answer += remainder
        storey //= 10

    return answer
print(solution(16))
