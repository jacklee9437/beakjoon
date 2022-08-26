from sys import stdin
input = stdin.readline

K, N = map(int,input().split())

lines = [int(input()) for _ in range(K)]

left = 1
right = max(lines)
answer = 0

def check(N, mid, lines) :
    cnt = sum(map(lambda x : x//mid, lines))
    if cnt >= N :
        return True
    else :
        return False

while left <= right :
    mid = (left + right) // 2
    if check(N, mid, lines) :
        answer = mid
        left = mid + 1
    else :
        right = mid - 1

print(answer)