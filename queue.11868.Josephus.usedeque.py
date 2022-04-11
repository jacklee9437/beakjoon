from sys import stdin
from typing import Deque
input = stdin.readline

N, K = map(int,input().split())

que = Deque(range(1,N+1))
rst = []

while len(que) != 0 :
    que.rotate(-K+1)
    rst.append(que.popleft())

print("<" + ', '.join(map(str,rst)) + ">")








'''
🤔 문제정의를 잘 하자 🤔

입력 : 
출력 : 

찾아야하는 값 : 
알고리즘 : 

-----


-----

'''