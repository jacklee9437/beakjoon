from sys import stdin
input = stdin.readline

N, K = map(int,input().split())
I = [0]
T = [0]
for _ in range(K) :
    i, t = map(int,input().split())
    I.append(i)
    T.append(t)

dp = [[0] * (N+1) for _ in range(K+1)]

for k in range(1, K+1) :
    for n in range(1, N+1) :
        if n >= T[k] :
            dp[k][n] = max(dp[k-1][n], dp[k-1][n-T[k]] + I[k])
        else :
            dp[k][n] = dp[k-1][n]

print(dp[K][N])

