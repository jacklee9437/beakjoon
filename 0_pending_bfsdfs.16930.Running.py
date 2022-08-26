from collections import deque
from sys import stdin
input = stdin.readline

N, M, K = map(int, input().split())
gym = [input().rstrip() for _ in range(N)]
r1, c1, r2, c2 = map(int, input().split())
r1 -= 1
c1 -= 1
r2 -= 1
c2 -= 1

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

visited = [[-1] * M for __ in range(N)]

que = deque()
que.append((r1, c1))
visited[r1][c1] = 0

while que :
    r, c = que.popleft()
    if r == r2 and c == c2 :
        print(visited[r][c])
        exit(0)

    for i in range(4) :
        for j in range(1, K+1) :
            nr = r + dr[i] * j
            nc = c + dc[i] * j
            if 0 <= nr < N and 0 <= nc < M and gym[nr][nc] == "." :
                if visited[nr][nc] == -1 :
                    visited[nr][nc] = visited[r][c] + 1
                    que.append((nr, nc))
                elif visited[nr][nc] < visited[r][c] :
                    break
            else :
                break
else :
    print(-1)
