from collections import deque
from sys import stdin
input = stdin.readline

N = int(input())

cards = deque()
for i in range(1,N+1):
    cards.append(i)
    
ans = ""

while cards :
    ans += str(cards.popleft()) + " "
    cards.rotate(-1)
print(ans)




'''
🤔🤔🤔 문제정의를 잘 하자 🤔🤔🤔

입력 : 
출력 : 

찾아야하는 값 : 
알고리즘 : 

-----



-----


'''