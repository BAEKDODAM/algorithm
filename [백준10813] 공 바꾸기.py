'''
문제) 
    1-N이 적힌 바구니에 같은 번호의 공이 하나씩 들어있음
    M번 바구니 중 두 바구니를 선택하여 공 맞바꿈
    공 바꾸기를 모두 마쳤을 때 각 바구니에 들은 공 return
    1<=N<=100, 1<=M<=100
'''

N , M= map(int, input().split())
basket = list(range(N + 1))

for i in range(M):
    a, b = map(int, input().split())
    basket[a], basket[b] = basket[b], basket[a]

print(*basket[1:])