from collections import deque
from sys import stdin, maxsize
input = stdin.readline


N = int(input())
Map = [list(map(int,input().split())) for _ in range(N)]

cnt = 0

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

ans = 0

for rain in range(0,101) :
    cnt = 0
    temp = [[False] * N for _ in range(N)]
    for i in range(N) :
        for j in range(N) :
            if Map[i][j] > rain and not temp[i][j] :
                cnt += 1
                temp[i][j] = True
                que = deque()
                que.append((i,j))
                while que :
                    r, c = que.popleft()
                    for k in range(4) :
                        nr = r + dr[k]
                        nc = c + dc[k]
                        if 0 <= nr < N and 0 <= nc < N :
                            if Map[nr][nc] > rain and not temp[nr][nc]:
                                temp[nr][nc] = True
                                que.append((nr,nc))
    ans = max(ans,cnt)

print(ans)