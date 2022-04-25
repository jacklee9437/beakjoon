from sys import stdin, maxsize
input = stdin.readline

N = int(input())
registered = [list(map(int,input().split())) for _ in range(N)]

registered.sort()
registered.sort(key=lambda x: x[1])

ans = 1
end = registered[0][1]
for s, e in registered[1:] :
    if s >= end :
        ans += 1
        end = e

print(ans)