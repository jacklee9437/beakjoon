# from collections import deque
from sys import stdin
input = stdin.readline

N, L, R = map(int,input().split())
nations = [list(map(int,input().split())) for _ in range(N)]

days = 0

moveComplete = False;
while not moveComplete :
   visited = [[0]*N for _ in range(N)]
   moved = False
   for curR in range(N) :
      for curC in range(N) :
         if visited[curR][curC] :
            continue
         que = []
         que.append((curR,curC))
         visited[curR][curC] = 1
         # united = []
         totalPop = nations[curR][curC]
         # united.append((curR,curC))
         # while que :
         #    r, c = que.popleft()
         for r, c in que :
            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)] :
               nr = r + dr
               nc = c + dc
               if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] :
                  if L <= abs(nations[r][c] - nations[nr][nc]) <= R :
                     visited[nr][nc] = 1
                     # united.append(((nr,nc)))
                     totalPop += nations[nr][nc]
                     que.append((nr,nc))
         if len(que) > 1 :
            eachPopAfterMove = totalPop // len(que)
            for r, c in que :
               nations[r][c] = eachPopAfterMove
            moved = True
   if not moved :
      moveComplete = True
   else :
      days += 1
print(days)
