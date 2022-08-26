from sys import stdin, maxsize
input = stdin.readline
INF = maxsize

N = int(input())

dp = [INF] * (N+1)
dp[1] = 0

for i in range(2, N+1) :
    if i%3 == 0 :
        dp[i] = min(dp[i], dp[i//3] + 1)
    if i%2 == 0 :
        dp[i] = min(dp[i], dp[i//2] + 1)
    dp[i] = min(dp[i], dp[i-1] + 1)

route = [N]
n = N
while n > 1 :
    if n%3 == 0 and dp[n] - dp[n//3] == 1 :
        n = n//3
    elif n%2 == 0 and dp[n] - dp[n//2] == 1 :
        n = n//2
    else :
        if dp[n] - dp[n-1] == 1 :
            n = n - 1
    route.append(n) 

print(dp[N])
print(*route)
