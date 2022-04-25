from collections import deque
from sys import stdin
input = stdin.readline

N =int(input())
A, B = map(int,input().split())
M = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(M) :
    X, Y = map(int,input().split())
    graph[X].append(Y)
    graph[Y].append(X)


visit = [False] * (N+1)
que = deque()
que.append((A,0))
visit[A] = True

while que :
    p, cnt = que.popleft()
    if p == B :
        print(cnt)
        exit()
    for c in graph[p] :
        if not visit[c] : 
            visit[c] = True
            que.append((c,cnt+1))
else :
    print(-1)