from sys import stdin
input = stdin.readline

N = int(input())
A = tuple(sorted(map(int,input().split())))
M = int(input())
cases = tuple(map(int,input().split()))

# for case in cases :
    # print(1 if case in A else 0)

def binary_search(arr, key) :
    left = 0
    right = len(arr) - 1

    while True :
        ptr = (left + right) // 2
        if arr[ptr] == key : 
            return 1
        elif arr[ptr] > key :
            right = ptr - 1
        else :
            left = ptr + 1
        if left > right : return 0

for case in cases :
    print(binary_search(A, case))

