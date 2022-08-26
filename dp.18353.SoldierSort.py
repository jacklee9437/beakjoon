from sys import stdin
input = stdin.readline

N = int(input())
combatpower = list(map(int,input().split()))

dp = [1] * N

for i in range(1, N) :
    for j in range(i) :
        if combatpower[i] < combatpower[j] :
            dp[i] = max(dp[i], dp[j] + 1)

print(N-max(dp))