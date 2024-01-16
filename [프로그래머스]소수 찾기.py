'''
문제. 소수 찾기
    한자리 숫자가 적힌 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 찾기
    각 종이 조각에 적힌 숫자가 적힌 문자열 = numbers
    종이 조각으로 만들 수 있는 소수가 몇 개인지 return

    제한사항
    - 1 ≤  numbers ≤ 7
    - numbers는 0~9까지 숫자만으로 이루어져 있습니다.
    - "013"은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져있다는 의미

풀이. 
    1.  itertools의 permutations(순열) 사용
'''
from itertools import permutations
import math
def solution1(numbers):
    prime_set = set() # 집합 사용 -> 중복 값 제거

    # 모든 숫자 조합을 만든다
    list(numbers) # 문자열을 한 글자씩 담은 list가 생성됨
    for i in range(len(numbers)):
        numbers_permutations =  permutations(list(numbers), i+1)
        numbers_perm_set =list(map(int, map("".join, numbers_permutations)))
        prime_set |= set(numbers_perm_set)
    
    # 소수가 아닌 수를 제거한다
    prime_set -= set(range(0,2)) # 0, 1은 소수가 아니므로 제외
    lim = int(math.sqrt(max(prime_set))) + 1
    for i in range(2, lim):
        prime_set -= set(range(i*2, max(prime_set)+1, i))
    
    return len(prime_set)

# prime set을 정의
prime_set = set()  

def isPrime(number):
    # 0, 1 제외
    if number in (0,1):
        return False
    
    # 에라토스테네스의 체
    lim = int(math.sqrt(number)) + 1
    for i in range(2, lim):
        if number % i == 0:
            return False
    return True

def recursive(combination, others):
    # 탈출 조건
    if combination != "":
        if isPrime(int(combination)):
            prime_set.add(int(combination))
    
    # 현재까지 만들어진 숫자에 남아있는 숫자 중 하나를 더한다
    for i in range(len(others)):
        recursive(combination + others[i], others[:i] + others[i+1:])

def solution2(numbers):
    # 모든 조합을 만드는 recursive를 수행
    recursive("", numbers)

    # prime_set의 length를 반환
    return len(prime_set)
    
print(solution2("17"))