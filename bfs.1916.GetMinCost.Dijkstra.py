import heapq as hq
from sys import stdin, maxsize
input = stdin.readline

INF = maxsize

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(M) :
    S, E, C = map(int,input().split())
    graph[S].append((E,C))
PS, PE = map(int,input().split())

distance = [INF] * (N+1)



def dijkstra(start=PS) :
    que = []
    distance[PS] = 0
    hq.heappush(que, (0, start))
    while que :
        dist, now = hq.heappop(que)

        if distance[now] < dist : continue
        for i in graph[now] :
            cost = i[1] + dist
            if cost < distance[i[0]] :
                distance[i[0]] = cost
                hq.heappush(que, (cost, i[0]))

dijkstra()
print(distance[PE])




