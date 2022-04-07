from sys import stdin
input = stdin.readline

def set_pivot(l,m,r) :
    global arr
    if arr[l] > arr[m] : arr[l], arr[m] = arr[m], arr[l]
    if arr[m] > arr[r] : arr[m], arr[r] = arr[r], arr[m]
    if arr[l] > arr[m] : arr[l], arr[m] = arr[m], arr[l]
    return m


def quick(l,r) :
    global N, arr, left, right
    pl = l
    pr = r
    m = (l+r) // 2
    pivot = set_pivot(l,m,r)

    arr[pivot], arr[r-1] = arr[r-1], arr[pivot]
    pl += 1
    pr -= 2

    while pl <= pr :
        while arr[pl] < arr[r-1] : pl += 1
        while arr[pr] > arr[r-1] : pr -= 1
        if pl <= pr :
            arr[pl], arr[pr] = arr[pr], arr[pl]
            pl += 1
            pr -= 1

    if pr > l :
        quick(l,pr)
    if pl < r :
        quick(pl,r)
    

N = int(input())
arr = [int(input().strip()) for _ in range(N)]

left = 0
right = N-1

quick(left,right)

[print(arr[i]) for i in range(N)]