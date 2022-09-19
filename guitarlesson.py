from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
lectures = list(map(int, input().split()))

if N == 1 :
    print(lectures[0])
    exit(0)

left = 1
right = sum(lectures)
if M == 1 :
    print(right)
    exit(0)

ret = 0

while left <= right :
    mid = (left + right) // 2
    count = 1
    tmp = 0
    tmpMax = 0
    for lect in lectures :
        if tmp + lect <= mid :
            tmp += lect
        else :
            count += 1
            tmpMax = max(tmpMax, tmp)
            tmp = lect
    tmpMax = max(tmpMax, tmp)
    if count <= M :
        ret = mid
        right = mid - 1
    else :
        left = mid + 1

print(ret)