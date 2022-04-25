from sys import stdin
input = stdin.readline

N, K = map(int,input().split())
W = [0]
V = [0]
for _ in range(N) :
    w, v = map(int,input().split())
    W.append(w)
    V.append(v)

dp = [[0] * (K+1) for _ in range(N+1)]

for item in range(1, N+1) :
    for weight in range(1, K+1) :
        if W[item] <= weight :
            dp[item][weight] = max(dp[item-1][weight], dp[item-1][weight-W[item]] + V[item])
        else :
            dp[item][weight] = dp[item-1][weight]

print(dp[N][K])