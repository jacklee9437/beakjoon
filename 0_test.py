from sys import stdin, maxsize
input = stdin.readline

N = int(input())
W = [list(map(int,input().split())) for _ in range(N)]

dp = [[0] * (1<<N) for _ in range(N)]
MAX = maxsize

def go(now=0, visit=1) :
    if dp[now][visit] :
        return dp[now][visit]
    if visit == (1<<N) - 1 :
        return W[now][0] if W[now][0] > 0 else MAX
    cost = MAX
    for i in range(1,N) :
        if not visit & (1<<i) and W[now][i] != 0 :
            val = go(i, visit | (1<<i))
            cost = min(cost, val + W[now][i])
    
    dp[now][visit] = cost
    return dp[now][visit]

print(go())