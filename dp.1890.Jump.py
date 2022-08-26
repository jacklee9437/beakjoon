from sys import stdin, maxsize
input = stdin.readline
INF = maxsize

N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]

dp = [[0] * N for _ in range(N)]
dp[0][0] = 1

for i in range(0, N) :
    for j in range(0, N) :
        for k in range(0, i) :
            dp[i][j] += dp[k][j] if board[k][j] == i - k else 0
        for k in range(0, j) :
            dp[i][j] += dp[i][k] if board[i][k] == j - k else 0

print(dp[N-1][N-1])