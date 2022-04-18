from collections import deque
import heapq
from sys import stdin
input = stdin.readline

N, M, K, X = map(int,input().split())
nodes = [list() for _ in range(N+1)]
for _ in range(M) :
    A, B = map(int,input().split())
    nodes[A].append(B)

visit = [0] * (N+1)

def bfs(x=X) :
    que = deque()
    visit[x] = 1
    que.append(x)
    while que :
        v = que.popleft()
        for i in nodes[v] :
            if not visit[i] :
                visit[i] = visit[v] + 1
                que.append(i)

bfs()
print(visit)
if K+1 in visit :
    for i in range(N+1) :
        print(i) if visit[i] == K+1 else None
else :
    print(-1)





