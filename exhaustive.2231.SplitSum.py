from sys import stdin
input = stdin.readline

N = int(input())
ans = 0
for i in range(1, N) :
    if i + sum(map(int,str(i))) == N :
        ans = i
        break
print(ans)