from sys import stdin
input = stdin.readline

n = int(input())
triangle = [[0] for _ in range(n)]
for i in range(n) :
    triangle[i].extend(map(int,input().split()))
    triangle[i].append(0)

for i in range(1, n) :
    for j in range(1, i+2) :
        triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])

print(max(triangle[-1]))