from collections import deque
from sys import stdin
input = stdin.readline

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
degree = [0] * (N+1)
for _ in range(M) :
    X, Y, K = map(int,input().split())
    graph[Y].append((X, K))
    degree[X] += 1
rst = [[0] * N for _ in range(N+1)]
basic = []

que = deque()

for i in range(1,N+1) :
    if degree[i] == 0 :
        que.append(i)
        basic.append(i)

while que :
    v = que.popleft()
    for i, e in graph[v] :
        if v in basic :
            rst[i][v] = e
        else :
            for j in range(1,N) :
                rst[i][j] += rst[v][j] * e
        degree[i] -= 1
        if degree[i] == 0 :
            que.append(i)

for i in basic :
    print(i, rst[N][i])

