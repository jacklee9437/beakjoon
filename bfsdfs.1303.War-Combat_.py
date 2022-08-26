from collections import deque
from sys import stdin
input = stdin.readline

N, M = map(int,input().split())
soldiers = [input().rstrip() for _ in range(M)]
checked = [[0] * N for _ in range(M)]

camps = {"W" : [], "B" : []}

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

for r in range(M) :
    for c in range(N) :
        if checked[r][c] :
            continue
        checked[r][c] = 1
        camp = soldiers[r][c]
        cnt = 0
        que = deque()
        que.append((r, c))
        while que :
            tr, tc = que.popleft()
            cnt += 1
            for i in range(4) :
                nr = tr + dr[i]
                nc = tc + dc[i]
                if 0 <= nr < M and 0 <= nc < N and soldiers[nr][nc] == camp and not checked[nr][nc] :
                    checked[nr][nc] = 1
                    que.append((nr, nc))
        camps[camp].append(cnt)

print(sum(map(lambda x: x**2, camps["W"])), end=" ")
print(sum(map(lambda x: x**2, camps["B"])))