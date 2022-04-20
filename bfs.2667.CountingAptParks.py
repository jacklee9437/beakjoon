from collections import deque
from sys import stdin, maxsize
input = stdin.readline

N = int(input())
Map = [list(map(int,input().rstrip())) for _ in range(N)]

rst = []
parkCnt = 0

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

for i in range(N) :
    for j in range(N) :
        if Map[i][j] == 1 :
            Map[i][j] = 0
            parkCnt += 1
            houseCnt = 0
            que = deque()
            que.append((i,j))
            while que :
                r, c = que.popleft()
                houseCnt += 1
                for k in range(4) :
                    nr = r + dr[k]
                    nc = c + dc[k]
                    if 0 <= nr < N and 0 <= nc < N :
                        if Map[nr][nc] == 1 :
                            Map[nr][nc] = 0
                            que.append((nr,nc))
            rst.append(houseCnt)

print(parkCnt)
for i in sorted(rst) :
    print(i)