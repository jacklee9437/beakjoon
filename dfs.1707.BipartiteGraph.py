from sys import stdin, setrecursionlimit
input = stdin.readline

setrecursionlimit(10**6)

# 입력
K = int(input())
for _ in range(K) :
    V, E = map(int,input().split())
    nodes = [list() for _ in range(V+1)]
    for _ in range(E) :
        u,v = map(int,input().split())
        nodes[u].append(v)
        nodes[v].append(u)
    chkvisit = [False] * (V+1)
    chkBi = [0] * (V+1)

    def dfs(s, bool=True) :
        global chk
        chkvisit[s] = True
        chkBi[s] = 1 if bool else 2
        for i in nodes[s] :
            if chkvisit[i] == False :
                dfs(i, not bool)
            else :
                if chkBi[s] == chkBi[i] : chk = False
    
    chk = True
    
    for i in range(1,V+1) :
        if chkvisit[i] == False :
            dfs(i)
            if not chk : 
                print("NO")
                break
    else : print("YES")
