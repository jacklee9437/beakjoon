
import heapq as hq
from sys import stdin, maxsize
input = stdin.readline

N = int(input())
Matrix = [list(map(int,input().rstrip())) for _ in range(N)]
graph = [[] for _ in range(N+1)]
outdegree = [0] * (N+1)
for i in range(N) :
    for j in range(N) :
        if Matrix[i][j] == 1 :
            graph[j+1].append(i+1)
            outdegree[i+1] += 1

que = []
A = [0] * (N+1)

for i in range(1,N+1) :
    if outdegree[i] == 0 :
        hq.heappush(que,-i)

num = N
while que :
    big = -hq.heappop(que)
    A[big] = num
    num -= 1
    for small in graph[big] :
        outdegree[small] -= 1
        if outdegree[small] == 0 :
            hq.heappush(que,-small)

if 0 in A[1:] :
    print(-1)
else :
    print(*A[1:])