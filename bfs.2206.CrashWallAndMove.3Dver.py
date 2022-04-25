from heapq import heappop, heappush
from sys import stdin, maxsize
input = stdin.readline
INF = maxsize

N, M = map(int,input().split())
Map = [list(map(int,input().rstrip())) for _ in range(N)]

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

route = [[[INF] * 2 for _ in range(M)] for _ in range(N)]
route[0][0][1] = 1
que = []
heappush(que, (1,1,0,0))

while que :
    cnt, psbCrash, r, c  = heappop(que)
    if cnt > route[r][c][psbCrash] : continue
    for i in range(4) :
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < M :
            if not Map[nr][nc] :
                dist = cnt + 1
                if route[nr][nc][psbCrash] > dist :
                    route[nr][nc][psbCrash] = dist
                    heappush(que,(dist,psbCrash,nr,nc))
            else :
                if psbCrash :
                    dist = cnt + 1
                    if route[nr][nc][psbCrash-1] > dist :
                        
                        route[nr][nc][psbCrash-1] = dist
                        heappush(que,(dist,psbCrash-1,nr,nc))

ans = min(route[N-1][M-1][0],route[N-1][M-1][1])
print(ans if ans != INF else -1)