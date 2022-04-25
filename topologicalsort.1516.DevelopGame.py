from collections import deque
from sys import stdin, maxsize
input = stdin.readline

N = int(input())
Buildings = [[] for _ in range(N+1)]
indegree = [0] * (N+1)
times = [0] * (N+1)
que = deque()
for building in range(1,N+1) :
    ipt = list(map(int,input().split()))
    if len(ipt) == 2 :
        times[building] = ipt[0]
        que.append(building)
    else :
        time = ipt[0]
        needs = ipt[1:-1]
        for need in needs :
            Buildings[need].append((building,time))
            indegree[building] += 1
        
while que :
    need = que.popleft()
    for needfor, time in Buildings[need] :
        times[needfor] = max(times[needfor], times[need] + time)
        indegree[needfor] -= 1
        if indegree[needfor] == 0 :
            que.append(needfor)

print(*times[1:],sep="\n")