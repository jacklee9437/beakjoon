from sys import stdin
input = stdin.readline

n = int(input())
papers = sorted([list(sorted(map(int, input().split()))) for _ in range(n)])

dp = [1 for _ in range(n)]

for i in range(1, n) :
    for j in range(i) :
        if papers[j][1] <= papers[i][1] :
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))