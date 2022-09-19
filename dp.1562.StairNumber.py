from sys import stdin
input = stdin.readline

N = int(input())
dp = [[[0] * (1 << 10) for _ in range(10)] for __ in range(N+1)]

for i in range(1, 10) :
    dp[1][i][1 << i] = 1

for l in range(2, N+1) :
    for e in range(10) :
        for b in range(1 << 10) :
            if e == 0 :
                dp[l][e][b | 1 << e] += dp[l-1][e+1][b]
            elif e == 9 :
                dp[l][e][b | 1 << e] += dp[l-1][e-1][b]
            else :
                dp[l][e][b | 1 << e] += dp[l-1][e+1][b]
                dp[l][e][b | 1 << e] += dp[l-1][e-1][b]

answer = 0
for e in range(10) :
    answer += dp[N][e][(1 << 10) - 1]
    answer %= 1000000000
print(answer)