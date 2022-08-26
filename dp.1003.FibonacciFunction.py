from sys import stdin, maxsize
input = stdin.readline
INF = maxsize

dp = [[0] * 2 for _ in range(41)]
dp[0][0] = 1
dp[0][1] = 0
dp[1][0] = 0
dp[1][1] = 1

idx = 2

for _ in range(int(input())) :
    N = int(input())

    for i in range(idx, N+1) :
        dp[i][0] = dp[i-1][0] + dp[i-2][0]
        dp[i][1] = dp[i-1][0] + dp[i][0]

    print(dp[N][0], dp[N][1])
    idx = N + 1 if N > 1 else 2