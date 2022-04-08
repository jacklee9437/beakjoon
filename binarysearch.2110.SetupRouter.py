from sys import stdin
input = stdin.readline

N, C = map(int,input().split())
x = tuple(sorted([int(input()) for _ in range(N)]))

left = 1
right = (x[-1]-x[0]) // (C-1) + 1

ans = 0

while left <= right :
    tempLen = (left + right) // 2
    
    curntP = x[0]
    cnt = 1
    
    for i in range(1, N) :
        if x[i] - curntP >= tempLen :
            cnt += 1
            curntP = x[i]
    
    if cnt >= C :
        ans = tempLen
        left = tempLen + 1
    else :
        right = tempLen - 1
    
print(ans)