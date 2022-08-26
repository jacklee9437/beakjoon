from sys import stdin
input = stdin.readline

n = int(input())
nums = list(map(int, input().split()))
dp = [nums[:] for _ in range(2)]

for i in range(1, n) :
    dp[0][i] = max(dp[0][i], dp[0][i-1]+dp[0][i])
    dp[1][i] = max(dp[0][i-1], dp[1][i-1]+dp[1][i], dp[1][i])

print(max(max(dp[0]), max(dp[1])))