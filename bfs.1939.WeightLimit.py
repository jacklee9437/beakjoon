from heapq import heappop, heappush
from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    A, B, C = map(int, input().split())
    graph[A].append((B, C))
    graph[B].append((A, C))
P1, P2 = map(int, input().split())

dist = [0] * (N+1)
que = []
heappush(que, (0, P1))

while que:
    ds, s = heappop(que)
    if -ds < dist[s]:
        continue
    if s == P2:
        break
    for e, w in graph[s]:
        d = w if not -ds else min(-ds, w)
        if dist[e] < d:
            dist[e] = d
            heappush(que, (-d, e))

print(dist[P2])
