from sys import stdin
input = stdin.readline

from math import trunc

N, M = map(int,input().split())
trs = tuple(map(int,input().split()))

start, end = 1, max(trs)


while start <= end :
    tempH = (start + end) // 2
    log = 0

    for tr in trs :
        if tr > tempH :
            log += tr - tempH
    
    if log >= M :
        start = tempH + 1
    elif log < M :
        end = tempH - 1

print(end)