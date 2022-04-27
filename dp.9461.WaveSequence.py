from sys import stdin, maxsize
input = stdin.readline

dp = [0] * (101)
dp[1] = 1
dp[2] = 1
dp[3] = 1

for _ in range(int(input())) :
    N = int(input())
    
    for i in range(4, N+1) :
        if not dp[i] :
            dp[i] = dp[i-3] + dp[i-2]

    print(dp[N])