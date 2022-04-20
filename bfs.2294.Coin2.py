from collections import deque
from sys import stdin, maxsize
input = stdin.readline

N, K = map(int,input().split())
coins = [int(input()) for i in range(N)]

que = deque()
chk = [False] * (K+1)

for coin in coins :
    if coin <= K :
        que.append([coin,1])
        chk[coin] = True

while que :
    val, cnt = que.popleft()
    if val == K :
        print(cnt)
        break
    for coin in coins :
        rst = val + coin
        Cnt = cnt + 1
        if rst > K :
            continue
        if not chk[rst] :
            que.append([rst,Cnt])
            chk[rst] = True
else :
    print(-1)

