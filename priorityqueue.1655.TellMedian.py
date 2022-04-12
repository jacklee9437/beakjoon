import heapq as hq
from sys import stdin
input = stdin.readline

N = int(input())
leftMaxHeap = []
rightMinHeap = []

for i in range(1,N+1) :
    cmd = int(input())
    if i%2 == 1 :
        hq.heappush(leftMaxHeap,-cmd)
    else :
        hq.heappush(rightMinHeap,cmd)
    
    if i > 1 and -leftMaxHeap[0] > rightMinHeap[0] :
        hq.heappush(leftMaxHeap,-hq.heappop(rightMinHeap))
        hq.heappush(rightMinHeap,-hq.heappop(leftMaxHeap))
    
    print(-leftMaxHeap[0])

    


'''
🤔 문제정의를 잘 하자 🤔

입력 : 백준이가 외치는 정수의 개수 N, 백준이가 외치는 점수들
출력 : 백준이 동생이 말해야하는 수

찾아야하는 값 : 
알고리즘 : 우선순위 큐,,,

-----
자료구조 문제의 경우, 자료구조 그대로를 쓴다기보다는 원리를 활용해서 어떻게 써먹을 것인가 인듯 한데,,
우선순위 큐를 heapq로 구현한다 쳤을때, 이 문제는 중간값을 빼와야 함.
최대heap 의 구조를 보면, 트리의 부모노드는 자식노드보다 크다는 규칙이 있지만, 자식노드간에는 어떤 규칙이 없음. -> 힙으로 정렬된 배열에서 어느 위치에서 빼오기는 어렵지 않겠나,,
그러면 그대로 쓰기보다는 뭔가 변형?이 필요해보이는데..
단순히 값만 따지면 최대값을 구하는거지만, key와 value 구조로 본다면 key를 우선순위에 따라 정렬할 수 있을듯 함
그러면 어떻게 정수의 중간값에 우선순위를 줘서 heap 구조로 만들 수 있을까...

중간값은 계속 변하고, 그럼 우선순위도 변할텐데..?
힙에서 계속 key 값을 바꾸지는 않을 듯 함...

또다른 생각,, 자료구조는 데이터를 저장하려는 의미도 있겠지만, 그보단 문제해결과정에 써먹기 위함임. 임시 저장용일 수 있다는 점,,
스택은 LIFO, 큐는 FIFO 구조라는 점을 이용했다면,
우선순위 큐는 FIFO 인 점과 heap이라는 점을 활용할 수 있을듯..

최소가 유지된다면 heappush 해도 배열이 바뀌진 않음
최소가 들어가거나 heappop을 하면 배열이 바뀜,,

임시로 저장해서 사용할 방법..?



결국 답 봄 ㅠ


우선순위 큐는 최대힙 or 최소힙 임. 중간값을 어떻게 빼냄!!! 그래서 두개를 합침.
최대힙 / 최소힙 합쳐서 끝에 있는게 중간값이 되게 해주면 됨!
-----

'''