from collections import deque
from sys import stdin, maxsize
input = stdin.readline

R, C = map(int,input().split())
Map = [list(input().rstrip()) for i in range(R)]

exodus = [[maxsize] * C for _ in range(R)]
dr = [-1, 0, 1, 0]
dc = [0, 1,  0, -1]

que = deque()
for i in range(R) :
    for j in range(C) :
        if Map[i][j] == "S" :
            que.append(("Gosmi",(i,j)))
            exodus[i][j] = 0
        elif Map[i][j] == "*" :
            que.appendleft(("Wave",(i,j)))
            exodus[i][j] = -1
        elif Map[i][j] == "X" :
            exodus[i][j] = -1

while que :
    obj, rc = que.popleft()
    for i in range(4) :
        nr = rc[0] + dr[i]
        nc = rc[1] + dc[i]
        if 0 <= nr < R and 0 <= nc < C :
            if obj == "Gosmi" :
                if Map[nr][nc] == "*" or exodus[nr][nc] < exodus[rc[0]][rc[1]]:
                    continue
                else :
                    if Map[nr][nc] == "D" :
                        print(exodus[rc[0]][rc[1]]+1)
                        exit()
                    exodus[nr][nc] = exodus[rc[0]][rc[1]] + 1
                    que.append((obj, (nr,nc)))
            else :
                if Map[nr][nc] == "*" or Map[nr][nc] == "X" or Map[nr][nc] == "D" :
                    continue
                else :
                    Map[nr][nc] = "*"
                    que.append((obj, (nr,nc)))
else :
    print("KAKTUS")

# for i in range(R) :
#     print(Map[i])
#     print(exodus[i])