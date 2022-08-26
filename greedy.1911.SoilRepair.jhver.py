from sys import stdin
input = stdin.readline

N, L = map(int,input().split())
pools = [list(map(int,input().split())) for _ in range(N)]
pools.sort()
installed = 0
cnt = 0
for s, e in pools :
    if installed >= s :
        s = installed
    need, r = divmod(e-s,L)
    if r :
        need += 1
    cnt += need
    installed = s + need * L

print(cnt)