from sys import stdin
input = stdin.readline

N, L = map(int,input().split())
pools = [list(map(int,input().split())) for _ in range(N)]
pools.sort(reverse=True, key=lambda x:x[1])
installed = pools[0][1]
cnt = 0

for pool in pools :
    s, e = pool
    e -= 1

    while s <= e :
        if e == installed :
            installed -= L
            e -= L
            cnt += 1
        elif e < installed :
            installed = e-L
            e -= L
            cnt += 1
        else :
            e = installed 

print(cnt)
