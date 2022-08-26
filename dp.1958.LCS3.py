from sys import stdin
input = stdin.readline

s1 = input().rstrip()
s2 = input().rstrip()
s3 = input().rstrip()

dp = [[[0 for _ in range(len(s3)+1)] for __ in range(len(s2)+1)] for ___ in range(len(s1)+1)]
for x in range(1, len(s1)+1) :
    for y in range(1, len(s2)+1) :
        for z in range(1, len(s3)+1) :
            if s1[x-1] == s2[y-1] == s3[z-1] :
                dp[x][y][z] = dp[x-1][y-1][z-1] + 1
            else :
                dp[x][y][z] = max(dp[x][y][z-1], dp[x][y-1][z], dp[x-1][y][z], dp[x][y-1][z-1], dp[x-1][y-1][z], dp[x-1][y][z-1])

print(dp[len(s1)][len(s2)][len(s3)])