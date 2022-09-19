from sys import stdin
input = stdin.readline

N = int(input())
Arr = list(map(int, input().split()))
if N == 1 :
    print(0)
    exit(0)

swapCount = 0

def mergeSort(left, right) :
    global swapCount
    if left >= right :
        return
    
    mid = (left + right) // 2
    mergeSort(left, mid)
    mergeSort(mid+1, right)
    l, r = left, mid+1
    tmp = []
    while l <= mid and r <= right :
        if Arr[l] <= Arr[r] :
            tmp.append(Arr[l])
            l += 1
        else :
            tmp.append(Arr[r])
            swapCount += mid+1 - l
            r += 1
    while l <= mid :
        tmp.append(Arr[l])
        l += 1
    while r <= right :
        tmp.append(Arr[r])
        r += 1
    for i in range(left, right + 1) :
        Arr[i] = tmp[i-left]

mergeSort(0, N-1)
print(swapCount)