from sys import stdin
input = stdin.readline

def binary_search(arr, key) :
    left = 0
    right = len(arr) - 1
    

    while True :
        chk_idx = (left + right) // 2
        if arr[chk_idx] == key :
            return chk_idx
        if arr[chk_idx] > key :
            right = chk_idx-1
        else :
            left = chk_idx+1
        if left > right : return -1

N, C = map(int,input().split())
x = tuple(sorted([int(input()) for _ in range(N)]))

left = 0
right = (x[-1]- x[0]) // C

tempLen = (left + right) // 2

while left <= right :
    pl = pr = 0
    count = 2
    for i in range(N-1) :
        pl = i
        pr = binary_search(x, x[i]+tempLen)
        if pr :
            break
    if x[pl]-x[0] < (C-2) * tempLen :
        if x[-1]-x[pr] < (C-2) * tempLen : right = tempLen - 1
        else :
            for i in range(pr+1,N) :
                if x[i] - x[pr] >= tempLen :
                    pr = i
                    count += 1

'''
tempLen 의 간격이 있는지를 먼저 찾고 그 왼쪽, 오른쪽으로 그보다 큰 값들이 C-2개 있는지 찾으려는 concept 이었으나
pl,pr 두 위치를 찾는 것도 비용이 들고, 그 왼쪽 오른쪽을 추가 확인하는데에도 비용이 많이 들어 비효율적인듯 함.
이방법은 pass...

차라리 처음부터 확인해서 C개를 설치할 수 있는지 확인하는게 더효율적인듯 - 인터넷...
'''






    # if True : 
    #     left = tempLen + 1
    # else :
    #     right = tempLen - 1
    
