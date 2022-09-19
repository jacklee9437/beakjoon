from collections import deque
from sys import stdin
input = stdin.readline

N, P = map(int, input().split())
c = [[0] * (N+1) for _ in range(N+1)]
graph = [[] for _ in range(N+1)]
for _ in range(P) :
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    c[a][b] = 1

f = [[0] * (N+1) for _ in range(N+1)]

cnt = 0
while True :
    prev = [-1] * (N+1)
    prev[1] = 0
    que = deque([1])
    while que :
        city = que.popleft()
        if city == 2 :
            break
        for to in graph[city] :
            if to == 1 : continue
            if prev[to] == -1 and c[city][to] - f[city][to] > 0 :
                prev[to] = city
                que.append(to)
    if prev[2] == -1 :
        break

    minFlow = float('inf')
    i = 2
    while prev[i] :
        minFlow = min(minFlow, c[prev[i]][i] - f[prev[i]][i])
        i = prev[i]

    i = 2
    while prev[i] :
        f[prev[i]][i] += minFlow
        f[i][prev[i]] -= minFlow
        i = prev[i]

    cnt += minFlow

print(cnt)