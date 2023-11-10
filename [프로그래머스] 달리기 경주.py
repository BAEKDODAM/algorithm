'''
[프로그래머스] 달리기 경주

틀린 풀이)
callings를 반복문으로 돌며 players에 해당 선수의 이름 인덱스를 찾고
앞 인덱스 선수와 swap 해주었는데시간초과가 발생했다

풀이)

'''

# 시간초과
def solution0(players, callings):
    for i in callings:
        idx = players.index(i)
        players[idx-1], players[idx] = players[idx], players[idx-1]

    return players

def solution(players, callings):
    playerDic = {player : i for i, player in numerate(players)}
    indexDic = {i : player for i, player in numerate(players)}

    for name in callings:
        rank = playerDic[name] # 현재 등수
        frontPlayer = indexDic[rank-1] # 앞 선수
        
        indexDic[rank] = frontPlayer
        indexDic[rank-1] = name

        playerDic[name] = rank-1
        playerDic[frontPlayer] = rank
    

print(solution(["mumu", "soe", "poe", "kai", "mine"], ["kai", "kai", "mine", "mine"]))

