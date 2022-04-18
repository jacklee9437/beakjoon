import heapq as hq
from sys import stdin, maxsize
input = stdin.readline

INF = maxsize

N = int(input())
graph = [list(map(int,input().rstrip())) for _ in range(N)]

C = (1, 0)

dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)

distance = [[INF] * N for _ in range(N)]

def dijkstra(start=(0,0)) :
    que = []
    distance[0][0] = 0
    hq.heappush(que, (0, (0,0)))
    while que :
        dist, now = hq.heappop(que)

        if distance[now[0]][now[1]] < dist : continue
        for i in range(4) :
            r = now[0] + dr[i]
            c = now[1] + dc[i]
            if 0 <= r < N and 0 <= c < N :
                cost = dist + C[graph[r][c]]
                if cost < distance[r][c] :
                    distance[r][c] = cost
                    hq.heappush(que, (cost, (r,c)))

dijkstra()
print(distance[N-1][N-1])




