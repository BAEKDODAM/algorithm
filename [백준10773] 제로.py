'''
    숫자 들어오면 스택에 add
    입력에 0이 들어오면 스택에 들어있는 숫자 하나 pop
'''

N = int(input())
stack = []
for _  in range(N):
    num = int(input())
    if num==0:
        stack.pop()
    else: stack.append(num)
print(sum(stack))