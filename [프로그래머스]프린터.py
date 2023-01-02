'''
중요도 높은 문서 먼저 인쇄
1. 인쇄 대기목록의 가장 앞에 있는 문서(J)를 대기목록에서 꺼냄
2. 나머지 인쇄 대기목록에서 J보다 중요도가 높은 문서가
   한 개라도 존재하면 J를 대기목록의 가장 마지막에 넣습니다.
3. 그렇지 않으면 J를 인쇄합니다.
'''
def sol(priorities, location):
    answer = 0
    queue = priorities
    a = []
    i=0
    while len(a)!=len(priorities):
        if queue[0] < max(queue[1:]) :
            queue.append(queue[0])
            queue.pop(0)
        else :
            queue.pop(0)
            queue.append(0)
            a.append(i%len(priorities))
        print("#",i,queue)
        i+=1
    print("a",a)
    answer = a.index(location)+1
    print(answer)
    return answer

def solution(priorities, location):
    answer = 0
    queue = priorities
    a = []
    for i in range(len(priorities)):
        if queue[0] < max(queue[1:]) :
            queue.append(queue[0])
            queue.pop(0)
        else :
            queue.pop(0)
            queue.append(0)
            a.append(i)
        print("#",i,queue)
    print("a",a)
    return answer

sol([1, 1, 9, 1, 1, 1]	,0)
