from sys import stdin, setrecursionlimit, maxsize
input = stdin.readline

setrecursionlimit(10**6)

N = int(input())
A = list(map(int,input().split()))
opers = list(map(int,input().split()))

m = maxsize
M = -maxsize

def dfs(depth, cal, plus, minus, multiply, devide) :
    global M, m

    if depth == N :
        m = min(m,cal)
        M = max(M,cal)

    else :
        if plus : dfs(depth+1, cal+A[depth], plus-1, minus, multiply, devide)
        if minus : dfs(depth+1, cal-A[depth], plus, minus-1, multiply, devide)
        if multiply : dfs(depth+1, cal*A[depth], plus, minus, multiply-1, devide)
        if devide : dfs(depth+1, cal//A[depth] if cal>0 else -((-cal)//A[depth]), plus, minus, multiply, devide-1)

plus, minus, multiply, devide = opers
dfs(1,A[0],plus,minus,multiply,devide)
print(M)
print(m)













