from collections import deque
from sys import stdin
input = stdin.readline

N, M = map(int,input().split())
miro = [list(map(int,input().strip())) for _ in range(N)]

visit = [[0]*M for _ in range(N)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def bfs(i=0,j=0) :
    global visit
    que = deque()
    visit[i][j] = 1
    que.append((i,j))
    cnt = 2
    while que :
        a,b = que.popleft()
        if a == N-1 and b == M-1 :
            break
        chk = False
        for d in range(4) :
            r = a + dr[d]
            c = b + dc[d]
            if 0 <= r < N and 0 <= c < M :
                if miro[r][c] and not visit[r][c] :
                    visit[r][c] = visit[a][b] + 1
                    que.append((r,c))
    return visit[N-1][M-1]


print(bfs())





