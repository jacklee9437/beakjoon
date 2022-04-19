from copy import deepcopy
from sys import stdin, maxsize
input = stdin.readline

N, M = map(int,input().split())
iceberg = [list(map(int,input().split())) for _ in range(N)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def melt() :
    global iceberg
    tempIceberg = deepcopy(iceberg)
    for i in range(1, N-1) :
        for j in range(1, M-1) :
            if iceberg[i][j] != 0 :
                for k in range(4) :
                    nr = i + dr[k]
                    nc = j + dc[k]
                    if iceberg[nr][nc] == 0 :
                        tempIceberg[i][j] -= 1 if tempIceberg[i][j] > 0 else 0
    iceberg = deepcopy(tempIceberg)

year = 1
while True :
    melt()

    cnt = 0
    visit = [[False] * M for _ in range(N)]
    for i in range(1, N-1) :
        for j in range(1, M-1) :
            if iceberg[i][j] != 0 and not visit[i][j]:
                stk = []
                stk.append((i,j))
                while stk :
                    r, c = stk.pop()
                    visit[r][c] = True
                    for k in range(4) :
                        nr = r + dr[k]
                        nc = c + dc[k]
                        if iceberg[nr][nc] != 0 and not visit[nr][nc] :
                            stk.append((nr,nc))
                cnt += 1

    if cnt == 0 :
        print(0)
        exit()
    elif cnt > 1 :
        print(year)
        exit()

    year += 1
