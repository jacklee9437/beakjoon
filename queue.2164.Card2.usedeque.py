from sys import stdin
from typing import Deque
input = stdin.readline

N = int(input())
que = Deque(range(1,N+1),maxlen=N)


while len(que) > 1 :
    que.popleft()
    que.append(que.popleft())

print(que.pop())






'''
🤔 문제정의를 잘 하자 🤔

입력 : 
출력 : 

찾아야하는 값 : 
알고리즘 : 

-----


-----

'''