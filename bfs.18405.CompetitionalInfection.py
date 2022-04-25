from collections import deque
from sys import stdin
input = stdin.readline

N, K = map(int, input().split())
tubes = []
que = []
for i in range(N):
    I = list(map(int, input().split()))
    for j in range(N):
        if I[j] != 0:
            que.append((I[j], (i, j), 0))
    tubes.append(I)
S, X, Y = map(int, input().split())

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

que = deque(sorted(que))
while que:
    k, rc, sec = que.popleft()
    r, c = rc
    if sec == S:
        print(tubes[X-1][Y-1])
        exit()
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < N:
            if tubes[nr][nc] == 0:
                tubes[nr][nc] = k
                que.append((k, (nr, nc), sec+1))
else:
    print(tubes[X-1][Y-1])
