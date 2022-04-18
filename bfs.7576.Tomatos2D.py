from collections import deque
from sys import stdin, maxsize
input = stdin.readline

M, N = map(int,input().split())
tomatos = [list(map(int,input().split())) for i in range(N)] # tomatos[N][M]

done = [[maxsize] * M for _ in range(N)]
dr = [-1, 0, 1, 0]
dc = [0, 1,  0, -1]

que = deque()
for i in range(N) :
    for j in range(M) :
        if tomatos[i][j] == 1 :
            que.append((i,j))
            done[i][j] = 0
        elif tomatos[i][j] == -1 :
            done[i][j] = -1

while que :
    r, c = que.popleft()
    for i in range(4) :
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < M :
            if tomatos[nr][nc] == -1 :
                continue
            else :
                if done[r][c] + 1 < done[nr][nc] :
                    done[nr][nc] = done[r][c] + 1
                    que.append((nr,nc))

days = 0
for i in range(N) :
    days = max(days, max(done[i]))
if days == maxsize :
    print(-1)
else :
    print(days)