from heapq import heapify, heappop
from collections import deque
from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]

islands = [[0] * M for _ in range(N)]

countIslands = 0
for curR in range(N) :
    for curC in range(M) :
        if Map[curR][curC] == 0 or islands[curR][curC] : continue
        
        countIslands += 1
        islands[curR][curC] = countIslands
        que = deque()
        que.append((curR, curC))
        while que :
            r, c =que.popleft()
            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)] :
                nr = r + dr
                nc = c + dc
                if 0 <= nr < N and 0 <= nc < M and Map[nr][nc] and islands[nr][nc] == 0 :
                    islands[nr][nc] = countIslands
                    que.append((nr, nc))

bridges = [{} for _ in range(countIslands + 1)]
for i in range(1, countIslands+1) :
    for j in range(1, countIslands+1) :
        bridges[i][j] = 1e9

for curR in range(N) :
    leftIsland = 0
    leftLocation = 0
    for curC in range(M) :
        if Map[curR][curC] == 0 : continue
        if islands[curR][curC] == leftIsland :
            leftLocation = curC
            continue

        if leftIsland == 0 :
            leftIsland = islands[curR][curC]
            leftLocation = curC
            continue
        
        if curC - leftLocation > 2 :
            bridges[leftIsland][islands[curR][curC]] = min(curC - leftLocation - 1, bridges[leftIsland][islands[curR][curC]])
        leftIsland = islands[curR][curC]
        leftLocation = curC

for curC in range(M) :
    upIsland = 0
    upLocation = 0
    for curR in range(N) :
        if Map[curR][curC] == 0 : continue
        if islands[curR][curC] == upIsland :
            upLocation = curR
            continue

        if upIsland == 0 :
            upIsland = islands[curR][curC]
            upLocation = curR
            continue
        
        if curR - upLocation > 2 :
            bridges[upIsland][islands[curR][curC]] = min(curR - upLocation - 1, bridges[upIsland][islands[curR][curC]])
        upIsland = islands[curR][curC]
        upLocation = curR

graph = []
for i, d in enumerate(bridges[1:], 1) :
    for k in d.keys() :
        graph.append((d[k], i, k))

heapify(graph)
parent = [i for i in range(countIslands+1)]

def find(c) :
    if parent[c] != c :
        parent[c] = find(parent[c])
        return parent[c]
    return c

def union(a, b) :
    if find(a) != find(b) :
        parent[parent[a]] = parent[b]
        return True
    return False

dist = 0
while graph :
    d, a, b = heappop(graph)
    if union(a, b) :
        dist += d

if dist > 1e9 :
    dist = -1

print(dist)