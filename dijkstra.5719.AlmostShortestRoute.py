from collections import deque
from heapq import heappush, heappop
from sys import stdin, maxsize
input = stdin.readline
INF = int(maxsize)

def dijkstra(N, S, D) :
    distance = [INF] * N
    distance[S] = 0
    minHeap = [(0, S)]
    while minHeap :
        d, s = heappop(minHeap)
        if distance[s] < d :
            continue
        if s == D :
            return distance
        for dd, e in forwardGraph[s] :
            if (tmp := d + dd) < distance[e] and edgeCheck[s][e]:
                distance[e] = tmp
                heappush(minHeap, (tmp, e))
    return distance

while True :
    N, M = map(int, input().split())
    if N + M == 0 :
        break

    S, D = map(int, input().split())
    forwardGraph = [[] for _ in range(N)]
    reverseGraph = [[] for _ in range(N)]
    edgeCheck = [[False] * N for _ in range(N)]

    for _ in range(M) :
        U, V, P = map(int, input().split())
        forwardGraph[U].append((P, V))
        edgeCheck[U][V] = True
        reverseGraph[V].append((P, U))

    distance = dijkstra(N, S, D)
    shortest = distance[D]
    if shortest == INF :
        print(-1)
        continue

    que = deque([(D, shortest)])
    while que :
        s, d = que.popleft()
        for dd, e in reverseGraph[s] :
            if distance[e] + dd == d and edgeCheck[e][s]:
                edgeCheck[e][s] = False
                que.append((e, distance[e]))

    ret = dijkstra(N, S, D)[D]
    print(ret if ret != INF else -1)

