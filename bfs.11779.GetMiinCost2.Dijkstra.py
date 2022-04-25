from collections import deque
from heapq import heappop, heappush
from sys import stdin, maxsize
input = stdin.readline
INF = maxsize

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
backGraph = [[] for _ in range(N+1)]
for _ in range(M) :
    S, E, C = map(int,input().split())
    graph[S].append((C,E))
    backGraph[E].append((C,S))
Lv, Arv = map(int,input().split())

distance = [INF] * (N+1)

que = []
distance[Lv] = 0
heappush(que,(0,Lv))
while que :
    d, s = heappop(que)
    if d > distance[s] : continue
    for c, e in graph[s] :
        cost = d + c
        if cost < distance[e] :
            distance[e] = cost
            heappush(que,(cost,e))
            
route = [Arv]
visit = [False] * (N+1)
que = deque()
que.append(Arv)
while que :
    e = que.popleft()
    if e == Lv : 
        route.reverse()
        break
    for c, s in backGraph[e] :
        if distance[e] - distance[s] == c :
            route.append(s)
            if not visit[s] : 
                que.append(s)
            break
print(distance[Arv])
print(len(route))
print(*route)