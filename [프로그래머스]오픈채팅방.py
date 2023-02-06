'''
[프로그래머스] 오픈채팅방
dict에 아이디와 닉네임 저장하여 닉네임 변경시 dict 수정

Enter 입장
Leave 퇴장
Change 닉네임 변경
'''


def solution(record):
    answer = []
    chatRoom = {}
    for i in record:
        info = i.split(' ')
        if info[0] == 'Enter':
            chatRoom[info[1]] = info[2]
        elif info[0] == 'Change':
            chatRoom[info[1]] = info[2]
    for j in record:
        info = j.split(' ')
        name = chatRoom[info[1]]
        w = ""
        if info[0] == 'Enter':
            w = name+"님이 들어왔습니다."
            answer.append(w)
        elif info[0] == 'Leave':
            w = name+"님이 나갔습니다."
            answer.append(w)
    return answer
print(solution(["Enter uid1234 Muzi",
                "Enter uid4567 Prodo",
                "Leave uid1234",
                "Enter uid1234 Prodo",
                "Change uid4567 Ryan"]))
