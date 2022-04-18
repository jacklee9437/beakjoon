from collections import deque
from sys import stdin
input = stdin.readline

s = input().strip()
bombStr = input().strip()

lenBS = len(bombStr)

stk = deque()

for char in s:
    if char != bombStr[-1] :
        stk.append(char)
        continue

    stk.append(char)
    if ''.join(stk[-lenBS:]) == bombStr:
        for _ in range(lenBS):
            stk.pop()

if not stk:
    print("FRULA")
else:
    print(''.join(stk))
