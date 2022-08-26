from sys import stdin
input = stdin.readline

N = int(input())
ropes = [int(input()) for _ in range(N)]
ropes.sort(reverse=True)

maxweight = 0
for i in range(N, 0, -1) :
    maxweight = max(maxweight, ropes.pop() * i)
print(maxweight)
