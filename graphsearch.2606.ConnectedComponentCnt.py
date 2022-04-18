from sys import stdin, setrecursionlimit
input = stdin.readline

setrecursionlimit(10**6)

# 입력
N, M = map(int,input().split())
li = [list() for _ in range(N+1)]
for _ in range(M) :
    u, v = map(int,input().split())
    li[u].append(v)
    li[v].append(u)
chkvisit = [False] * (N+1)

def dfs(s) :
    chkvisit[s] = True
    for i in li[s] :
        if chkvisit[i] == False :
            dfs(i)

cntCC = 0
for i in range(1, N+1) :
    if chkvisit[i] == False :
        dfs(i)
        cntCC += 1
print(cntCC)
