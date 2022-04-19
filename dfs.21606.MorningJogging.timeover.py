from sys import stdin, setrecursionlimit
input = stdin.readline

setrecursionlimit(10**6)

# 입력
N = int(input())
A = " " + input().strip()
nodes = [list() for _ in range(N+1)]
for _ in range(N-1) :
    u,v = map(int,input().split())
    nodes[u].append(v)
    nodes[v].append(u)

# 스택방법
def dfs_stk(s) :
    global cnt, A
    stk.append(s)
    v = 1
    while stk :
        p = stk.pop()
        chkvisit[p] = True
        if v!=1 and A[p]=="1" :
            cnt+=1
            continue
        for i in nodes[p] :
            if not chkvisit[i] :
                v+=1
                stk.append(i)
        
# 재귀방법
def dfs(s, v=1) : 
    global cnt, A
    chkvisit[s] = True
    if v!=1 and A[s]=='1' :
        cnt += 1
        return
    for i in nodes[s] :
        if not chkvisit[i] :
            dfs(i, v+1)

stk = []

cnt = 0
if A.count("1") < 2  :
    print(0)
else : 
    for i in range(1,N+1) :
        if A[i] == '1' :
            chkvisit = [False] * (N+1)
            dfs_stk(i)

    print(cnt)


    ## 200점 위해 추가 구현 필요!!