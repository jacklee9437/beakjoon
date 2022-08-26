from sys import stdin
input = stdin.readline

n = int(input())
boxes = list(map(int,input().split()))

dp = [0] * n
dp[0] = 1

for i in range(1, n) :
    maxval = 0
    for j in range(i) :
        if boxes[j] < boxes[i] :
            maxval = max(maxval, dp[j])
    dp[i] = maxval + 1

print(max(dp))