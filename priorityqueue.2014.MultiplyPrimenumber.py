from copy import copy
import heapq as hq
from sys import stdin
input = stdin.readline

K, N = map(int, input().rstrip().split())  # K 소수의 개수, N N번째 수
primeNums = list(map(int, input().split()))

minHeap = copy(primeNums)
popCnt = 0
ans = 0

for i in range(N) :
    ans = hq.heappop(minHeap)
    popCnt += 1

    if popCnt == N : break

    for j in primeNums :
        hq.heappush(minHeap,ans * j)

        if ans % j == 0 :
            break

print(ans)