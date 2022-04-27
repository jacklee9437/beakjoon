from sys import stdin, maxsize
input = stdin.readline
INF = maxsize

N, M = map(int, input().split())
smalls = set([int(input()) for _ in range(M)])

dp = [[INF] * int(((2 * N) ** 0.5 + 2)) for _ in range(N+1)]
dp[1][0] = 0

for i in range(2, N+1) :
    if i in smalls :
        continue
    for j in range(1, int(((2 * i) ** 0.5 + 1))) :
        dp[i][j] = min(dp[i-j][j], dp[i-j][j-1], dp[i-j][j+1]) + 1

ans = min(dp[N])
print(*dp[2])
if ans == INF :
    print(-1)
else :
    print(ans)




