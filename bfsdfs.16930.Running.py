from collections import deque
from sys import stdin
input = stdin.readline

N, M, K = map(int, input().split())
gym = [input().rstrip() for _ in range(N)]
sr, sc, er, ec = map(lambda n : int(n)-1, input().split())

visited = [[float('inf')] * M for _ in range(N)]
dirx = [[1,0],[0,1],[-1,0],[0,-1]]

visited[sr][sc] = 0
que = deque([(sr, sc, 0)])
while que :
    r, c, t = que.popleft()
    if (r, c) == (er, ec) :
        print(t)
        break
    if t > visited[r][c] :
        continue
    
    nt = t + 1
    for dr, dc in dirx :
        for k in range(1, K+1) :
            nr = r + dr * k
            nc = c + dc * k
            if 0 <= nr < N and 0 <= nc < M and gym[nr][nc] == "." :
                if visited[nr][nc] == nt:
                    continue
                elif visited[nr][nc] > nt:
                    visited[nr][nc] = nt
                    que.append((nr, nc, nt))
                elif visited[nr][nc] <= t:
                    break
            else :
                break
else :
    print(-1)