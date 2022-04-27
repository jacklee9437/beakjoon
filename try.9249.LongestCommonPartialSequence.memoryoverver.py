from sys import stdin, maxsize
input = stdin.readline

str1 = " " + input().rstrip()
str2 = " " + input().rstrip()
lenStr1 = len(str1)-1
lenStr2 = len(str2)-1
if lenStr1 > lenStr2 :
    str1, str2 = str2, str1
    lenStr1, lenStr2 = lenStr2, lenStr1

dp = [[0] * (lenStr2 + 1) for _ in range(lenStr1 + 1)]

for i in range(1,lenStr1 + 1) :
    for j in range(1, lenStr2 + 1) :
        chr1 = str1[i]
        chr2 = str2[j]
        if chr1 == chr2 :
            dp[i][j] = dp[i-1][j-1] + 1

# print(*dp,sep='\n')
print(max(dp[lenStr1]))