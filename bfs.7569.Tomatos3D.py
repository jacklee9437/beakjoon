from collections import deque
from sys import stdin, maxsize
input = stdin.readline

M, N, H = map(int,input().split())
tomatos = [[list(map(int,input().split())) for i in range(N)] for j in range(H)] # tomatos[H][N][M]

done = [[[maxsize] * M for i in range(N)] for j in range(H)]
dr = [-1, 0, 1, 0, 0, 0]
dc = [0, 1,  0, -1, 0, 0]
dh = [0, 0, 0, 0, 1, -1]

que = deque()
for i in range(H) :
    for j in range(N) :
        for k in range(M) :
            if tomatos[i][j][k] == 1 :
                que.append((i,j,k))
                done[i][j][k] = 0
            elif tomatos[i][j][k] == -1 :
                done[i][j][k] = -1

while que :
    h, r, c = que.popleft()
    for i in range(6) :
        nh = h + dh[i]
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < M and 0 <= nh < H :
            if tomatos[nh][nr][nc] == -1 :
                continue
            else :
                if done[h][r][c] + 1 < done[nh][nr][nc] :
                    done[nh][nr][nc] = done[h][r][c] + 1
                    que.append((nh,nr,nc))

days = 0
for i in range(H) :
    for j in range(N) :
        days = max(days, max(done[i][j]))
if days == maxsize :
    print(-1)
else :
    print(days)