N = int(input())
strSeq = list(map(int, input().split()))
revSeq = list(reversed(strSeq))

dp = [[0] * (N+1) for _ in range(N+1)]

for i in range(1, N+1) :
    for j in range(1, N+1) :
        if revSeq[i-1] == strSeq[j-1] :
            dp[i][j] = dp[i-1][j-1] + 1
        else :
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(N-dp[N][N])