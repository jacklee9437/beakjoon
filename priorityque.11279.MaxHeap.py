import heapq as hq
from sys import stdin
input = stdin.readline

N = int(input())
maxHeap = []

for _ in range(N) :
    cmd = int(input())
    
    if cmd == 0 :
        if len(maxHeap) == 0 :
            print(0)
        else :
            print(-hq.heappop(maxHeap))
    else :
        hq.heappush(maxHeap, -cmd)
    

    


'''
🤔 문제정의를 잘 하자 🤔

입력 : 연산의 개수 N, 연산에 대한 정보를 나타내는 정수 x
출력 : 0이 주어진 회수만큼 답 출력. 배열이 비어있는 경우에는 0 출력

찾아야하는 값 : 
알고리즘 : 

-----


-----

'''