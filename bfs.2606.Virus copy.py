from collections import deque
from sys import stdin
input = stdin.readline

computers = int(input())
n = int(input())
graph = [[] for _ in range(computers+1)]
for _ in range(n) :
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (computers + 1)

que = deque()
que.append(1)

visited[1] = 1

while que :
    k = que.popleft()
    for i in graph[k] :
        if not visited[i] :
            visited[i] = 1
            que.append(i)

print(sum(visited)-1)