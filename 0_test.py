from sys import stdin
input = stdin.readline

N = int(input())
visited = [0] * (N+1)

def backtrack(cur, N, buf) :
    if cur == N+1 :
        print(*buf)
        return
    
    for i in range(1, N+1) :
        if visited[i] :
            continue
        visited[i] = 1
        backtrack(cur+1, N, buf + [i])
        visited[i] = 0

backtrack(1, N, [])