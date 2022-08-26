from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
r, c, d = map(int, input().split())
map = [list(map(int,input().split())) for _ in range(N)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
cnt = 0

stateComplete = False
while not stateComplete : 
    map[r][c] = 2
    
    cnt += 1

    stateFound = False
    while not stateFound :
        for _ in range(4) :
            d = d - 1 if d > 0 else 3
            if map[r + dr[d]][c + dc[d]] :
                continue
            stateFound = True
            break
        else :
            if map[r - dr[d]][c - dc[d]] == 1 :
                stateComplete = True
                break
            else :
                r -= dr[d]
                c -= dc[d]
    r += dr[d]
    c += dc[d]

print(cnt)
