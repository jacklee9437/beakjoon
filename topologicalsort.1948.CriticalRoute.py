from collections import deque
import heapq
from sys import stdin
input = stdin.readline

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
backGraph = [[] for _ in range(N+1)]
degree = [0] * (N+1)
for _ in range(M) :
    S, E, T = map(int,input().split())
    graph[S].append((E, T))
    backGraph[E].append((S, T))
    degree[E] += 1
Lv, Arv = map(int, input().split())
rst = [0] * (N+1)

que = deque()

que.append(Lv)
while que :
    s = que.pop()
    for e, t in graph[s] :
        degree[e] -= 1
        rst[e] = max(rst[e], rst[s] + t)
        if degree[e] == 0 :
            que.append(e)

visit = [False] * (N+1)
que.append(Arv)
cnt = 0
while que :
    e = que.popleft()
    for s, t in backGraph[e] :
        if t == rst[e] - rst[s] :
            cnt += 1
            if not visit[s] :
                visit[s] = True
                que.append(s)
                
print(rst[Arv])
print(cnt)

