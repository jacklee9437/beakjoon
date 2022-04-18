from collections import deque
from copy import deepcopy
from sys import stdin, setrecursionlimit
input = stdin.readline

# 입력
N, M, V = map(int,input().split())
graph = [list() for _ in range(N+1)]
for _ in range(0,M) :
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(1, N+1) :
    graph[i].sort()
isvisited = [False] * (N+1)


def resetVisit() :
    global isvisited
    isvisited = [False] * (N+1)

def dfs(s) :
    isvisited[s] = True
    print(s, end=" ")
    for c in graph[s] :
        if isvisited[c] == False :
            dfs(c)

def bfs(s) :
    que = deque([s])
    isvisited[s] = True
    while que :
        s = que.popleft()
        print(s, end=" ")
        for i in graph[s] :
            if isvisited[i] == False :
                isvisited[i] = True
                que.append(i)
                

    
dfs(V)
resetVisit()
print()
bfs(V)
