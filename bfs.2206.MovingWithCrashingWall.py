from collections import deque
from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
Map = [input().rstrip() for _ in range(N)]
visited = [[[0 for _ in range(M)] for __ in range(N)] for ___ in range(2)]

que = deque([(1, 0, 0)])
visited[1][0][0] = 1
dirx = [[1,0],[0,1],[-1,0],[0,-1]]

while que :
    crashable, r, c = que.popleft()
    for dr, dc in dirx :
        nr = r + dr
        nc = c + dc
        if 0 <= nr < N and 0 <= nc < M :
            if not int(Map[nr][nc]) :
                if not visited[crashable][nr][nc] :
                    visited[crashable][nr][nc] = visited[crashable][r][c] + 1
                    que.append((crashable, nr, nc))
            else :
                if crashable and not visited[not crashable][nr][nc]:
                    visited[crashable^1][nr][nc] = visited[crashable][r][c] + 1
                    que.append((crashable^1, nr, nc))

noncrash = visited[1][N-1][M-1] if visited[1][N-1][M-1] else float('inf')
crash = visited[0][N-1][M-1] if visited[0][N-1][M-1] else float('inf')
answer = min(noncrash, crash)
print(answer if answer != float('inf') else -1)