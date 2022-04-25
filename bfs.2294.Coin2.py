from collections import deque
from sys import stdin, maxsize
input = stdin.readline

N, K = map(int,input().split())
coins = [int(input()) for _ in range(N)]

que = deque()
visit = [False] * (K+1)

que.append((0,0))

while que :
    k, cnt = que.popleft()
    if k == K :
        print(cnt)
        exit()
    for coin in coins :
        tempK = k + coin
        if tempK > K : continue
        if not visit[tempK] :
            visit[tempK] = True
            que.append((tempK,cnt+1))
else :
    print(-1)