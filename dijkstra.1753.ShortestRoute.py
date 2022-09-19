from heapq import heappush, heappop
from sys import stdin
input = stdin.readline

V, E = map(int,input().split())
K = int(input())
graph = [[] for _ in range(V + 1)]
for _ in range(E) :
    u, v, w = map(int,input().split())
    graph[u].append((w, v))

distance = [int(1e9) for _ in range(V + 1)]
distance[K] = 0

que = []
que.append((0, K))

while que :
    d, s = heappop(que)
    if distance[s] < d :
        continue
    for dist, e in graph[s] :
        n_d = d + dist
        if distance[e] > n_d :
            distance[e] = n_d
            heappush(que, (n_d, e))

for ans in distance[1:] :
    if ans == int(1e9) :
        print("INF")
    else :
        print(ans)