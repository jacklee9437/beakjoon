import heapq as hq
from sys import stdin
input = stdin.readline

N = int(input())
minHeap = []

for _ in range(N) :
    arr = tuple(map(int,input().split()))

    if not minHeap :
        for num in arr :
            hq.heappush(minHeap,num)
    else :
        for num in arr :
            if num > minHeap[0] :
                hq.heappush(minHeap,num)
                hq.heappop(minHeap)
print(minHeap[0])
            


'''
🤔🤔🤔 문제정의를 잘 하자 🤔🤔🤔

입력 : 
출력 : 

찾아야하는 값 : 
알고리즘 : 

-----



-----


'''