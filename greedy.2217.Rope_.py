from sys import stdin
input = stdin.readline

N = int(input())
ropes = [int(input()) for _ in range(N)]
ropes.sort()

ans = 0

for i in range(N) :
    n = N - i
    ans = max(ans, ropes[i] * n)
    
print(ans)