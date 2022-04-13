from collections import deque
from sys import stdin
input = stdin.readline

N = int(input())
towers = tuple(map(int,input().split()))

stk = deque()

for idx, tower in enumerate(towers,1) :
    while stk and stk[-1][1] <= tower :
        stk.pop()

    if not stk :
        print(0,end=" ")
    else : 
        print(stk[-1][0], end=" ")
    stk.append((idx,tower))