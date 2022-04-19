from collections import deque
import heapq
from sys import stdin
input = stdin.readline

N = int(input())
Matrix = [list(map(int,input().rstrip())) for _ in range(N)]
graph = [[] for _ in range(N+1)]
degree = [0] * (N+1)
for i in range(N) :
    for j in range(N) :
        if Matrix[i][j] == 1 :
            graph[j+1].append(i+1)
            degree[i+1] += 1

que = []

for i in range(1,N+1) :
    if degree[i] == 0 :
        heapq.heappush(que,-i)

num = N
rst = [0] * (N+1)
while que :
    v = -heapq.heappop(que)
    rst[v] = num
    num -= 1
    for i in graph[v] :
        degree[i] -= 1
        if degree[i] == 0 :
            heapq.heappush(que,-i)

if 0 in rst[1:] :
    print(-1)
else :
    print(' '.join(map(str,rst[1:])))

