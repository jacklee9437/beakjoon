from collections import deque
from sys import stdin
input = stdin.readline

N, K = map(int,input().split())
num = input().strip()

stk = deque()
tempK = 0

for n in num :
    while stk and stk[-1] < n :
        if tempK < K :
            tempK += 1
            stk.pop()
        else :
            break
    stk.append(n)

print(''.join(list(stk)[:N-K]))
