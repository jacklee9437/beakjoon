from sys import stdin, maxsize
input = stdin.readline
INF = int(maxsize)

n = int(input())
m = int(input())
dp = [[INF] * n for _ in range(n)]
for _ in range(m) :
    a, b, c = map(int, input().split())
    dp[a-1][b-1] = min(dp[a-1][b-1], c)
for i in range(n) :
    dp[i][i] = 0

for k in range(n) :
    for i in range(n) :
        for j in range(n) :
            if (tmp := dp[i][k] + dp[k][j]) < dp[i][j] :
                dp[i][j] = tmp

for i in range(n) :
    for j in range(n) :
        if dp[i][j] == INF :
            dp[i][j] = 0

for i in range(n) :
    print(*dp[i])

