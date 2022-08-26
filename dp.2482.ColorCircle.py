from sys import stdin
input = stdin.readline

N = int(input())
K = int(input())

dp = [[0 for _ in range(N+1)] for __ in range(K+1)]

for n in range(1, N+1) :
   dp[1][n] = n
dp[1][1] = 0

for k in range(2, K+1) :
   for n in range(1, N+1) :
      if k > n//2 :
         continue
      dp[k][n] = dp[k][n-1] + dp[k-1][n-2]

print(dp[K][N] % 1000000003)