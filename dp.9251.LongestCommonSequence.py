from sys import stdin
input = stdin.readline

str1 = ' ' + input().rstrip()
str2 = ' ' + input().rstrip()
lenStr1 = len(str1) - 1
lenStr2 = len(str2) - 1

dp = [[0] * (lenStr2+1) for _ in range(lenStr1+1)]

for i in range(1, lenStr1+1) :
    for j in range(1, lenStr2+1) :
        if str1[i] == str2[j] :
            dp[i][j] = max(dp[i][j-1], dp[i-1][j-1] + 1)
        else :
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])
ans = 0
for i in range(1,lenStr1+1) :
    ans = max(ans, dp[i][lenStr2])
print(ans)