import heapq as hq
from sys import stdin
input = stdin.readline

N = int(input())
minHeap = [int(input()) for _ in range(N)]

hq.heapify(minHeap)
compSum = 0

if N == 1 :
    compSum = 0
else :
    while len(minHeap) > 1 :
        min1 = hq.heappop(minHeap)
        min2 = hq.heappop(minHeap)
        temp = min1 + min2
        compSum += temp
        if not minHeap :
            break
        hq.heappush(minHeap,temp)


print(compSum)




'''
🤔 문제정의를 잘 하자 🤔

입력 : 숫자카드 묶음 수 N, 각 묶음별 카드 수 minHeap
출력 : 필요한 최소 비교 횟수

찾아야하는 값 : 
알고리즘 : 우선순위 큐

-----
재귀 냄새가 물씬 남. 반복문도 가능할듯.
N개 카드 중에 항상 최소 2개만 가지고 합을 구해줘야함.
- 두개를 합치면 그 합친게 섞어야하는 묶음 중의 또 한 묶음이 되기 때문에 다시 비교의 대상이 된다는 의미.
- 즉 일단 다 최소힙에 다 넣고, 순서대로 두개 빼서 더함. 그 더한건 비교 횟수가 되기때문에 일단 sum에 저장
- 그리고 다시 그 합친거가 비교대상이 되도록 힙에 넣음. 그러고 그 과정을 반복!


-----


'''