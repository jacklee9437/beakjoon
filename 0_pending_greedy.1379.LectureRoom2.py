from heapq import heappop ,heappush
from sys import stdin
input = stdin.readline

N = int(input())
lects = [list(map(int, input().split())) for _ in range(N)]
lects.sort(key=lambda x: (x[1],x[2]))

room = [i for i in range(1,N+1)]

minHeap = []

assigned = [i for i in range(N+1)]

for x in lects :
    lectNo, st, et = x
    while minHeap and minHeap[0][0] <= st :
        e, r = heappop(minHeap)
        heappush(room, r)

    r = heappop(room)
    heappush(minHeap, (et, r))
    assigned[lectNo] = r

print(max(assigned))
print(*assigned[1:],sep='\n')



'''
풀이 컨셉

1. N이 너무 커서 여러번 돌면 안된다. 한번에 스캔하면서 가야한다.
2. 조건에 맞지 않는 강의들을 다른 회의실에 어떻게 배정할지가 중요하다.
3. 조건에 맞지 않으면 다른 강의실에, 조건에 맞으면 같은 강의실에 배정해야한다.
4. 조건에 만족하지 않으면 해당 강의실을 배정할 수 없다 -> 조건에 맞는 강의실을 저장할 배열과 비교대상이 될 강의실(&조건)을 저장할 배열이 필요하다.
5. 낮은 회의실을 우선 배정하기 위해, 그리고 강의가 끝나는 시간이 이른 강의실부터 우선배정하기 위해 heap을 사용해야한다.
'''