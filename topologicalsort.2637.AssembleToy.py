from collections import deque
from sys import stdin, maxsize
input = stdin.readline

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
indegree = [0] * (N+1)
for _ in range(M) :
    X, Y, K = map(int,input().split())
    graph[Y].append((X,K))
    indegree[X] += 1

que = deque()
basic = []

cells = [[0] * N for _ in range(N+1)]

for i in range(1,N+1) :
    if indegree[i] == 0 :
        que.append(i)
        basic.append(i)

while que :
    need = que.popleft()
    for needfor, cnt in graph[need] :
        if need in basic :
            cells[needfor][need] = cnt
        else :
            for i in range(1,N) :
                cells[needfor][i] += cells[need][i] * cnt
        indegree[needfor] -= 1
        if indegree[needfor] == 0 :
            que.append(needfor)

for i in basic :
    print(i,cells[N][i])