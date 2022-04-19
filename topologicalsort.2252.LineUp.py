from collections import deque
from sys import stdin
input = stdin.readline

N, M = map(int,input().split())
graph = [[] for _ in range(N+1)]
degree = [0] * (N+1)
for _ in range(M) :
    A, B = map(int,input().split())
    graph[A].append(B)
    degree[B] += 1

que = deque()

# visit = [False] * (N+1)

for i in range(1,N+1) :
    if degree[i] == 0 :
        # visit[i] = True
        que.append(i)

while que :
    v = que.popleft()
    print(v,end=" ")
    for i in graph[v] :
        degree[i] -= 1
        if degree[i] == 0 :
            # visit[i] = True
            que.append(i)


