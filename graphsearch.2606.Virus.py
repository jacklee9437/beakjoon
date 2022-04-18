from sys import stdin, setrecursionlimit
input = stdin.readline

setrecursionlimit(10**6)

# 입력
N = int(input())
C = int(input())
li = [list() for _ in range(N+1)]
for _ in range(C) :
    u, v = map(int,input().split())
    li[u].append(v)
    li[v].append(u)
chkvisit = [False] * (N+1)

def dfs(s) :
    global cntCC
    chkvisit[s] = True
    cntCC+=1
    for i in li[s] :
        if chkvisit[i] == False :
            dfs(i)

cntCC = 0
dfs(1)
print(cntCC-1)
