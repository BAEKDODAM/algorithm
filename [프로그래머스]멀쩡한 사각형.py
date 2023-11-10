import math

def solution(w,h):
    g = h/w
    answer = 0
    if round(g) < g or g:
        answer = (round(g)+1)*w
    elif round(g) == g:
        answer = g*w
    else:
        answer = math.floor((round(g)+0.5)*w)
    print(g)
    return w*h-answer

print(solution(8,12))

if type('ss') == str:
    print('str')
