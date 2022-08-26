from collections import deque
from sys import stdin
input = stdin.readline

k = int(input())
signs = input().split()

asc = deque()
dsc = deque()

dsc.append(9)

for n, sign in enumerate(signs, 1) :
    n = 9 - n
    if sign == ">" :
        while asc :
            dsc.append(asc.popleft())
        dsc.append(n)
    else :
        asc.appendleft(dsc.pop())
        dsc.append(n)

while dsc :
    print(dsc.popleft(), end="")
while asc :
    print(asc.popleft(), end="")
print()

asc.append(0)

for n, sign in enumerate(signs, 1) :
    if sign == "<" :
        while dsc :
            asc.append(dsc.popleft())
        asc.append(n)
    else :
        dsc.appendleft(asc.pop())
        asc.append(n)

print(*asc, sep="", end="")
print(*dsc, sep="", end="")
