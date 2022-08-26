from sys import stdin
input = stdin.readline

N = int(input())
wines = [0] * 10001
for i in range(1, N+1) :
    wines[i] = int(input())

dp = [0] * 10001
dp[1] = wines[1]
dp[2] = wines[1] + wines[2]
dp[3] = max(dp[1] + wines[3], dp[2], wines[2] + wines[3])

for i in range(4, N+1) :
    dp[i] = max(dp[i-2] + wines[i], dp[i-1], dp[i-3] + wines[i-1] + wines[i])

print(max(dp))