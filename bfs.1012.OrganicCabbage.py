from collections import deque
from sys import stdin, maxsize
input = stdin.readline

T = int(input())
for _ in range(T) :
    M, N, K = map(int,input().split())
    Map = [[0] * M for _ in range(N)]
    for __ in range(K) :
        X, Y = map(int,input().split())
        Map[Y][X] = 1
    
    cnt = 0

    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    for i in range(N) :
        for j in range(M) :
            if Map[i][j] == 1 :
                Map[i][j] = 0
                cnt += 1
                que = deque()
                que.append((i,j))
                while que :
                    r, c = que.popleft()
                    for k in range(4) :
                        nr = r + dr[k]
                        nc = c + dc[k]
                        if 0 <= nr < N and 0 <= nc < M :
                            if Map[nr][nc] == 1 :
                                Map[nr][nc] = 0
                                que.append((nr,nc))

    print(cnt)