from bisect import bisect_left, bisect_right
from sys import stdin
input = stdin.readline

N = int(input())
A = tuple(sorted(map(int,input().split())))
M = int(input())
cases = tuple(map(int,input().split()))

# for case in cases :
    # print(1 if case in A else 0)

def binary_search(arr, key) :
    left = bisect_left(arr, key)
    right = bisect_right(arr, key)

    if left == right : 
        return False
    else :
        return True

for case in cases :
    print(1 if binary_search(A, case) else 0)

