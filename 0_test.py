from collections import deque
from sys import stdin, maxsize
input = stdin.readline

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
back_graph = [[] for _ in range(N+1)]
indegree = [0] * (N+1)
for _ in range(M) :
    S, E, T = map(int,input().split())
    graph[S].append((E,T))
    back_graph[E].append((S,T))
    indegree[E] += 1 
Lv, Arv = map(int,input().split())

times = [0] * (N+1)

que = deque()
que.append(Lv)

while que :
    s = que.popleft()
    for e, t in graph[s] :
        times[e] = max(times[e], times[s] + t)
        indegree[e] -= 1
        if indegree[e] == 0 :
            que.append(e)

cnt = 0
visit = [False] * (N+1)
que.append(Arv)
while que :
    e = que.popleft()
    for s, t in back_graph[e] :
        if times[e] - times[s] == t :
            cnt += 1
            if not visit[s] :
                visit[s] = True
                que.append(s)

print(times[Arv])
print(cnt)