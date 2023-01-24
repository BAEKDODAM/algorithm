'''
[프로그래머스] (2020 카카오 인턴십) 수식 최대화

문제)
연산의 우선순위를 마음대로 재정의하여(+, -, *)
주어진 수식의 결과를 구함
단, 수식 결과로 음수가 나올 경우 절댓값으로 변환하여 결과 구함
주어진 수식의 결과들 중 가장 큰 수 return

풀이)
1. itertools의 permutation을 사용하여 연산자의 우선순의의 모든 경우의 수를 구한다.
2. 모든 경우의 수를 다 계산하기 위한 for문을 작성한다
3. 먼저 3순위 연산자로 수식을 분리해준다
4. 2순의 연산자로 수식을 분리하고 각각 괄호로 묶어준 뒤 배열에 담는다
5. 배열을 join을 사용해 2순위 연산자를 사이에 넣어 합해주고 괄호 안에 담는다
6. 3순위 연산자를 사이에 넣어 join
7. eval 하여 문자열 안에 식을 계산한 뒤 abs를 사용하여 절댓값으로 변환하여 answer배열에 담는다
8. max(answer)하면 
'''
from itertools import permutations
def solution(expression):
    operators = ["*", "+", "-"]
    answer = []
    for oper in permutations(operators):
        tmp = []
        tmp_list = []
        for i in expression.split(oper[0]):
            tmp = [ "("+j+")" for j in i.split(oper[1]) ]
            tmp_list.append("("+oper[1].join(tmp)+")")
        answer.append(abs(eval(oper[0].join(tmp_list))))
    return max(answer)


print(solution2("100-200*300-500+20"))
