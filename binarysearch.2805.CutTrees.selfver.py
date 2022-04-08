from sys import stdin
input = stdin.readline

from math import trunc

N, M = map(int,input().split())
Trs = tuple(sorted(map(int,input().split())))

left = 0
right = N-1

ptr = 0
tempH = 0
tempM = 0
compM = False

while True :
    ptr = (left + right) // 2

    tempH = Trs[ptr]
    tempTrs = Trs[ptr+1:]
    tempM = sum(tempTrs) - (N-ptr-1) * tempH

    compM = tempM > M

    if tempM == M : break
    elif compM : left = ptr + 1
    else : right = ptr - 1

    if left > right : break

if left <= right : print(tempH)
else :
    if compM : print(trunc((sum(tempTrs)-M)/(N-ptr-1)))
    else : print(trunc((sum(Trs[ptr:])-M)/(N-ptr)))



