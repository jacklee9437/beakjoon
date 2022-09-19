from sys import stdin
input = stdin.readline

R, C = map(int, input().split())
Map = [list(input().rstrip()) for _ in range(R)]

def dfs(r, c) :
    if c == C-1 :
        return True
    
    for i in [-1, 0, 1] :
        rr, cc = r+i, c+1
        if 0 <= rr < R and Map[rr][cc] == "." :
            Map[rr][cc] = 'x'
            if dfs(rr, cc) :
                return True
    return False

answer = 0
for i in range(R) :
    if dfs(i, 0) :
        answer += 1
print(answer)