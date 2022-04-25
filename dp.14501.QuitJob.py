from sys import stdin, maxsize
input = stdin.readline
INF = maxsize

N = int(input())
T = []
P = []
for _ in range(N) :
    t, p = map(int,input().split())
    T.append(t)
    P.append(p)

# dp = [0] * (N+1) -> 조건문 하나 삭제 가능해짐.
dp = [0] * N

for i in range(N-1, -1, -1) :
    if i + T[i] < N :
        #  for j in range(i+T[i],N+1) :
            # dp[i] = max(dp[i],P[i] + dp[j])
        for j in range(i+T[i],N) :
            dp[i] = max(dp[i],P[i] + dp[j])
    # elif 문 삭제 가능
    elif i + T[i] == N :
        dp[i] = P[i]
    else :
        dp[i] = 0

print(max(dp))