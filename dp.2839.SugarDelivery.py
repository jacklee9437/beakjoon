from re import S
from sys import stdin, maxsize
input = stdin.readline
INF = maxsize

N = int(input())

dp = [INF] * (N+1) 
dp[0] = 0

for i in range(3, N+1) :
    dp[i] = min(dp[i-3] + 1, dp[i-5] + 1 if i >= 5 else INF)

if dp[N] >= INF :
    print(-1)
else :
    print(dp[N])