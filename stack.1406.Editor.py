from collections import deque
from sys import stdin
input = stdin.readline

str = input().rstrip()
M = int(input())
commandline = [input().rstrip() for _ in range(M)]

stk = list(str)
que = deque()

for cmd in commandline :
    if cmd[0] == "L" :
        if stk :
            que.appendleft(stk.pop())
    elif cmd[0] == "D" :
        if que :
            stk.append(que.popleft())
    elif cmd[0] == "P" :
        stk.append(cmd[-1])
    else :
        if stk :
            stk.pop()

answer = ''.join(stk) + ''.join(que)
print(answer)