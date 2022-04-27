from sys import stdin, maxsize
input = stdin.readline

N, T = map(int,input().split())
KSs = [0] + [list(map(int,input().split())) for _ in range(N)]

dp = [[0] * (T+1) for _ in range(N+1)]

for subject in range(1, N+1) :
    for time in range(1, T+1) :
        K, S = KSs[subject]
        if K <= time :
            dp[subject][time] = max(dp[subject-1][time],dp[subject-1][time-K] + S)
        else :
            dp[subject][time] = dp[subject-1][time]

print(dp[N][T])