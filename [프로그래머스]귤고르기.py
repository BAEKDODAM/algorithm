'''
[프로그래머스/python] 귤 고르기

풀이)

1. 귤의 종류와 갯수를 dict에 key와 요소로 담는다
2. sorted 를 사용하여 갯수가 큰 순으로 배열한다
3. 배열에서 갯수가 큰 것 부터 귤을 골라 담는다 생각하고 k에서 뺴준다.
   그리고 빼줄때마다 answer+1 해준다

'''

def solution(k, tangerine):
    answer=0
    tangerineDict = dict()
    for i in tangerine:
        if i in tangerineDict:
            tangerineDict[i]+=1
        else: tangerineDict[i]=1

    sortedDict = sorted(tangerineDict.items(), key=lambda item:item[1], reverse = True)

    for j in sortedDict:
        k -= j[1]
        answer+=1
        if k <= 0:
            return answer
        
'''

collections.Counter을 사용하면 시간복잡도를 줄일 수 있음
collections.Counter은 중복된 데이터가 저장된 배열을 인자로 넘기면
 각 원소가 몇 번씩 나오는지가 저장된 객체를 얻는다.
 (이 객체는 중복 데이터 많은 순으로 저장됨)

'''


import collections
def solution(k, tangerine):
    answer = 0
    cnt = collections.Counter(tangerine)
    print(cnt)
    for v in sorted(cnt.values(), reverse = True):
        k -= v
        answer += 1
        if k <= 0:
            break
    return answer
print(solutio(4, [1, 3, 2, 5, 4, 5, 2, 3]))
