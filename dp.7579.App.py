from sys import stdin
input = stdin.readline

N, M = map(int,input().split())
mem = [0] + list(map(int,input().split()))
cos = [0] + list(map(int,input().split()))

dp = [[0] * (sum(cos)+1) for _ in range(N+1)]

for i in range(1, N+1) :
    for j in range(1, sum(cos)+1) :
        if j >= cos[i] :
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-cos[i]] + mem[i])
        else :
            dp[i][j] = dp[i-1][j]

for i in range(1, sum(cos)+1) :
    for j in range(1, N+1) :
        if dp[j][i] >= M :
            print(i)
            exit()