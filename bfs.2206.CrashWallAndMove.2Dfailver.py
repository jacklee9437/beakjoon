from heapq import heappop, heappush
from sys import stdin, maxsize
input = stdin.readline
INF = maxsize

N, M = map(int,input().split())
Map = [list(map(int,input().rstrip())) for _ in range(N)]


dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def getMinDist(s,e) :
    global N,M
    route = [[INF]*M for _ in range(N)]
    route[s[0]][s[1]] = 1
    que = []
    heappush(que, (1,True,s[0],s[1]))

    while que :
        cnt, psbCrash, r, c  = heappop(que)
        if cnt > route[r][c] : continue
        for i in range(4) :
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M :
                if not Map[nr][nc] :
                    dist = cnt + 1
                    if route[nr][nc] > dist :
                        route[nr][nc] = dist
                        heappush(que,(dist,psbCrash,nr,nc))
                else :
                    if psbCrash :
                        dist = cnt + 1
                        if route[nr][nc] > dist :
                            route[nr][nc] = dist
                            heappush(que,(dist,not psbCrash,nr,nc))
    return route[e[0]][e[1]]
ans = min(getMinDist((0,0),(N-1,M-1)),getMinDist((N-1,M-1),(0,0)))
print(ans if ans != INF else -1)