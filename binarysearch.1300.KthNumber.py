from sys import stdin
input = stdin.readline

N = int(input())
k = int(input())
r = int(k ** (1/2))

rst = 0
left = 1
right = N*N
while left <= right :
    mid = (left + right) // 2

    cnt = 0
    for i in range(1, N+1) :
        cnt += min(N, mid//i)
    if cnt >= k :
        rst = mid
        right = mid - 1
    else :
        left = mid + 1

print(rst)