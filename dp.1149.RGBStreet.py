from sys import stdin, maxsize
input = stdin.readline

N = int(input())
costs = [[0,0,0]] + [list(map(int,input().split())) for _ in range(N)]
R = 0
G = 1
B = 2

dp = [[0] * 3 for _ in range(N+1)]
dp[1][R] = costs[1][R]
dp[1][G] = costs[1][G]
dp[1][B] = costs[1][B]

for i in range(2,N+1) :
    dp[i][R] = min(dp[i-1][G],dp[i-1][B]) + costs[i][R]
    dp[i][G] = min(dp[i-1][R],dp[i-1][B]) + costs[i][G]
    dp[i][B] = min(dp[i-1][G],dp[i-1][R]) + costs[i][B]

print(min(dp[N]))