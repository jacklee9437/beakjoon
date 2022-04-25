from collections import deque
from sys import stdin
input = stdin.readline

N, M = map(int,input().split())
graph = [[] for _ in range(N+1)]
indegree = [0] * (N+1)
for _ in range(M) :
    A, B = map(int,input().split())
    graph[A].append(B)
    indegree[B] += 1

que = deque()

for i in range(1,N+1) :
    if indegree[i] == 0 :
        que.append(i)

while que :
    v = que.popleft()
    print(v,end=" ")
    for i in graph[v] :
        indegree[i] -= 1
        if indegree[i] == 0 :
            que.append(i)


