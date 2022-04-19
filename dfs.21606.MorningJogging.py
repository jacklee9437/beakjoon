from collections import deque
from sys import stdin
input = stdin.readline

N = int(input())
A = list(map(int,("0" + input().rstrip())))
graph = [[] for _ in range(N+1)]
for _ in range(N-1) :
    u, v  = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

if A.count(1) < 2 : 
    print(0)
    exit()

visit = [False] * (N+1)

def dfs(exterior) :
    cnt = 0
    stk = []
    stk.append(exterior)
    while stk :
        v = stk.pop()
        visit[v] = True
        for c in graph[v] :
            if A[c] == 1 :
                cnt += 1
            else :
                if not visit[c] :
                    stk.append(c)
    return cnt

cnt = 0
for i in range(1,N+1) :
    if A[i] == 1 :
        for j in graph[i] :
            if A[j] == 1 :
                cnt += 1 
    else :
        if not visit[i] :
            temp = dfs(i)
            cnt += temp * (temp-1)

print(cnt)