from collections import deque
from sys import stdin
input = stdin.readline

T = int(input())

for _ in range(T) :
    N, M = map(int,input().split())
    que = deque()
    
    for point in map(int,input().split()) :
        que.append(point)

    printCnt = 0

    while True :
        while que[0] != max(que) :
            que.rotate(-1)
            M = (M - 1) % len(que)
        else :
            if M == 0 :
                printCnt += 1
                break
            que.popleft()
            printCnt += 1
            M = (M - 1) % len(que)

    print(printCnt)
    

    
    

    
        









'''

N번째 글자를 구하기 위해 필요한 k 값이 무엇인가를 찾아야 하는 문제 같은데..

N 값을 

또는,, 실제 수열이 어떻게 생겼느냐 하는 수열을 구하는 것과 상관없이, N번째 글자만 알 수 있는 방법이 있을까?


'''






































'''
🤔🤔🤔 문제정의를 잘 하자 🤔🤔🤔

입력 : 
출력 : 

찾아야하는 값 : 
알고리즘 : 

-----



-----


'''