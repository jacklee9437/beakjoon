from re import S
from sys import stdin, maxsize
input = stdin.readline
INF = maxsize

N = int(input())
A = [0] + list(map(int,input().split()))

dp = [1] * (N+1)

for i in range(2,N+1) :
    for j in range(1,i) :
        if A[j] > A[i] :
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))