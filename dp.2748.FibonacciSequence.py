from sys import stdin, maxsize
input = stdin.readline

N = int(input())

DP = [0, 1]

for i in range(2,N+1) :
    DP.append(DP[i-2] + DP[i-1])

print(DP[N])