from collections import deque
from sys import stdin, maxsize
input = stdin.readline

R, C = map(int,input().split())
Map = [list(input().rstrip()) for i in range(R)]

exodus = [[maxsize] * C for _ in range(R)]
dr = [-1, 0, 1, 0]
dc = [0, 1,  0, -1]

D = 0

que = deque()
for i in range(R) :
    for j in range(C) :
        if Map[i][j] == "S" :
            que.append((i, j))
            exodus[i][j] = 0
        elif Map[i][j] == "*" :
            que.appendleft((i, j))

while que :
    r, c = que.popleft()
    for i in range(4) :
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < R and 0 <= nc < C :
            if Map[r][c] == "S" :
                if Map[nr][nc] == "D" :
                    print(exodus[r][c]+1)
                    exit()
                if Map[nr][nc] == "." :
                    exodus[nr][nc] = exodus[r][c] + 1
                    Map[nr][nc] = "S"
                    que.append((nr, nc))
            else :
                if Map[nr][nc] == "." :
                    Map[nr][nc] = "*"
                    que.append((nr, nc))
else :
    print("KAKTUS")


# 시간초과의 원인
# 직관적인것도 좋지만, 가능하면 저장하는 임시 데이터가 적어야함.
#  -> 팝한게 고슴도치인지 물인지는 팝한 데이터에 있으면 메모리를 많이 차지하니까, 그보다는 있는 데이터를 활용하는게 좋음. 초기 데이터에 고슴도치와 물이 있으니까 거기다 추가하는게좋음.
# 비교연산이 적은게 좋음
#  -> 안되는걸 조건줘서 빼주는것도 좋지만, 가능하다면 되는 조건만 줘서 다른건 그냥 진행되지 않는 방식으로,,
