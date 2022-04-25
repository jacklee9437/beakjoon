from heapq import heappop, heappush
from sys import stdin, maxsize
input = stdin.readline
INF = maxsize

V, E = map(int,input().split())
K = int(input())
graph = [[] for _ in range(V+1)]
for _ in range(E) :
    u, v, w = map(int,input().split())
    graph[u].append((w,v))

distance = [INF] * (V+1)

def daijkstra(lv) :
    que = []
    distance[lv] = 0
    heappush(que,(0,lv))
    while que :
        d, s = heappop(que)
        if d > distance[s] : continue
        for w, e in graph[s] :
            cost = d + w
            if cost < distance[e] :
                distance[e] = cost
                heappush(que,(cost,e))

daijkstra(K)
for dist in distance[1:] :
    print(dist if dist != INF else "INF")