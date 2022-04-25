from collections import deque
from sys import stdin, maxsize
input = stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]
indegree = [0] * (N+1)
times = [0] * (N+1)
que = deque()
for work in range(1,N+1) :
    I = list(map(int,input().split()))
    time = I[0]
    if I[1] == 0 :
        times[work] = time
        que.append(work)
    else : 
        for k in range(I[1]) :
            worked = I[2+k]
            graph[worked].append((work,time))
            indegree[work] += 1

while que :
    worked = que.popleft()
    for work, time in graph[worked] :
        times[work] = max(times[work], times[worked] + time)
        indegree[work] -= 1
        if indegree[work] == 0 :
            que.append(work)

print(max(times))