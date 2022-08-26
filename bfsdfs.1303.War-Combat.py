from collections import deque
from sys import stdin
input = stdin.readline

N, M = map(int,input().split())
battleground = [list(input().rstrip()) for _ in range(M)]
visited = [[0 for _ in range(N)] for __ in range(M)]

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

soldiers = {"W" : [], "B" : []}

for chk_r in range(M) :
   for chk_c in range(N) :
      if visited[chk_r][chk_c] :
         continue

      visited[chk_r][chk_c] = 1
      count = 1
      que = deque()
      que.append((chk_r,chk_c))
      while que:
         r, c = que.popleft()
         for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < M and 0 <= nc < N and battleground[r][c] == battleground[nr][nc] and not visited[nr][nc] :
               visited[nr][nc] = 1
               count+=1
               que.append((nr, nc))
      soldiers[battleground[chk_r][chk_c]].append(count)

ans = [sum(map(lambda x : x**2, soldiers["W"])),sum(map(lambda x : x**2, soldiers["B"]))]
print(*ans)

