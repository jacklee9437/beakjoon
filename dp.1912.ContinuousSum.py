from sys import stdin, maxsize
input = stdin.readline

N = int(input())
seq = [0] + list(map(int,input().split()))

dp = [0] * (N+1)
dp[1] = seq[1]

for i in range(2, N+1) :
    if seq[i] >= dp[i-1] + seq[i] :
        dp[i] = seq[i]
    else :
        dp[i] = dp[i-1] + seq[i]

print(max(dp[1:]))