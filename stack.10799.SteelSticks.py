from collections import deque
from sys import stdin
input = stdin.readline

perens = input().strip()
stk = deque()

sticks = -1
pieces = 0

for idx, peren in enumerate(perens) :
    if peren == "(" :
        stk.append(peren)
        sticks += 1
        continue

    if perens[idx-1] == "(" :
        pieces += sticks
    else :
        pieces += 1
    sticks -= 1
    stk.pop()
    
print(pieces)



'''
🤔🤔🤔 문제정의를 잘 하자 🤔🤔🤔

입력 : 
출력 : 

찾아야하는 값 : 
알고리즘 : 

-----



-----


'''