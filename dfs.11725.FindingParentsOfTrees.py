from sys import stdin, setrecursionlimit
input = stdin.readline

setrecursionlimit(10**6)

# 입력
N = int(input())
nodes = [list() for _ in range(N+1)]
for _ in range(N-1) :
    u,v = map(int,input().split())
    nodes[u].append(v)
    nodes[v].append(u)
chkvisit = [False] * (N+1)

# family = []
family = [i for i in range(N+1)]
def dfs(s) :
    chkvisit[s] = True
    for i in nodes[s] :
        if chkvisit[i] == False :
            family[i] = s
            dfs(i)

dfs(1)
# family.sort()
for i in range(2,N+1) :
    print(family[i])
